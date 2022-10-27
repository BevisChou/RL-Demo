from enum import IntEnum
import json
import random

import gym
import numpy as np
import zmq

class RequestType(IntEnum):
    RESET = 0
    STEP = 1
    CLOSE = 2

class Config(object):
    pass

class CustomEnv(gym.Env):
    metadata = {"render.modes": ["human"]}

    def __init__(self):
        super(CustomEnv, self).__init__()

        self.action_space = gym.spaces.Box(low=np.array([-1]), high=np.array([1]), dtype=np.float32)
        self.observation_space = gym.spaces.Box(low=np.array([-np.pi / 4, -np.inf]), high=np.array([np.pi / 4, np.inf]), dtype=np.float32)

        self.eps = 1e-3

        self.config = Config()
        self.config.g = 9.8
        self.config.k = 1
        self.config.m = 1
        self.config.l = 1
        if bool(random.getrandbits(1)):
            self.config.w = random.uniform(0.2, 0.3)
        else:
            self.config.w = random.uniform(-0.5, -0.4)

        self.max_steps = 5000

        self.context = zmq.Context()
        self.socket = self.context.socket(zmq.PAIR)
        self.socket.connect("tcp://127.0.0.1:5555")

    def step(self, action):
        self.step_count += 1

        request = {
            "type": RequestType.STEP,
            "action": { "f": float(action[0]) }
        }
        self.socket.send_string(json.dumps(request))

        message = self.socket.recv()
        response = json.loads(message)

        observation = np.array([response["state"]["angle"], response["state"]["angular_velocity"]], dtype=np.float32)
        reward = self.calc_reward(observation)
        done = self.is_done(observation)
        info = {
            "r": reward,
            "f": action[0],
            "a": observation[0],
            "av": observation[1]
        }

        return observation, reward, done, info

    def reset(self, is_test=False):
        self.is_test = is_test
        request = {
            "type": RequestType.RESET,
            "mode": self.is_test,
            "config": {
                "g": self.config.g,
                "k": self.config.k,
                "m": self.config.m,
                "l": self.config.l,
                "w": self.config.w
            }
        }
        self.socket.send_string(json.dumps(request))

        message = self.socket.recv()
        response = json.loads(message)

        self.continuous_stability = 0
        self.step_count = 0

        observation = np.array([response["state"]["angle"], response["state"]["angular_velocity"]], dtype=np.float32)
        return observation

    def render(self, mode="human"):
        pass

    def close (self):
        request = {
            "type": RequestType.CLOSE
        }
        self.socket.send_string(json.dumps(request))

    def calc_reward(self, observation):
        if abs(observation[0]) > np.pi / 4:
            reward = -1e6
        elif self.continuous_stability > 25:
            reward = 1e6
        else:
            reward = 100 * (np.cos(observation[0]) - 1) * self.config.l * self.config.m * self.config.g - np.power(self.config.l * observation[1], 2) * self.config.m / 2
        return reward

    def stable_criteria(self, observation):
        return abs(observation[0]) < self.eps

    def done_criteria(self, observation):
        if self.stable_criteria(observation):
            self.continuous_stability += 1
        else:
            self.continuous_stability = 0
        
        if abs(observation[0]) > np.pi / 4:
            return True
        elif self.continuous_stability > 25:
            return True
        else:
            return False
    
    def is_done(self, observation):
        if not self.is_test and self.step_count > self.max_steps:
            return True
        else:
            return self.done_criteria(observation)
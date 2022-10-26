import gym
import numpy as np
import zmq

import msg_pb2

class CustomEnv(gym.Env):
    metadata = {"render.modes": ["human"]}

    def __init__(self):
        super(CustomEnv, self).__init__()

        self.action_space = gym.spaces.Box(low=np.array([-1]), high=np.array([1]), dtype=np.float32)
        self.observation_space = gym.spaces.Box(low=np.array([-np.pi / 4, -np.inf]), high=np.array([np.pi / 4, np.inf]), dtype=np.float32)

        self.eps = 1e-3

        self.config = msg_pb2.Request.Config()
        self.config.g = 9.8
        self.config.k = 1
        self.config.m = 1
        self.config.l = 1
        self.config.w = 0.1

        self.max_steps = 1000

        self.context = zmq.Context()
        self.socket = self.context.socket(zmq.PAIR)
        self.socket.connect("tcp://127.0.0.1:5555")

    def step(self, action):
        self.step_count += 1

        request = msg_pb2.Request()
        request.type = msg_pb2.Request.RequestType.STEP
        request.action = action[0]
        self.socket.send(request.SerializeToString())

        message = self.socket.recv()
        response = msg_pb2.Response()
        response.ParseFromString(message)

        observation = np.array([response.state.angle, response.state.angular_velocity], dtype=np.float32)
        if abs(observation[0]) < self.eps:
            self.continuous_stability += 1
        else:
            self.continuous_stability = 0

        reward = 100 * (np.cos(observation[0]) - 1) * self.config.l * self.config.m * self.config.g - np.power(self.config.l * observation[1], 2) * self.config.m / 2

        done = False
        info = {
            "r": reward,
            "f": action[0],
            "a": observation[0],
            "av": observation[1]
        }

        if abs(observation[0]) > np.pi / 4:
            reward = -1e3
            done = True
        elif self.continuous_stability > 20:
            reward = 1e3
            done = True
        elif self.step_count > self.max_steps:
            done = True

        return observation, reward, done, info

    def reset(self):
        request = msg_pb2.Request()
        request.type = msg_pb2.Request.RequestType.RESET
        request.config.CopyFrom(self.config)
        self.socket.send(request.SerializeToString())

        message = self.socket.recv()
        response = msg_pb2.Response()
        response.ParseFromString(message)

        self.continuous_stability = 0
        self.step_count = 0

        observation = np.array([response.state.angle, response.state.angular_velocity], dtype=np.float32)
        return observation

    def render(self, mode="human"):
        pass

    def close (self):
        request = msg_pb2.Request()
        request.type = msg_pb2.Request.RequestType.CLOSE
        self.socket.send(request.SerializeToString())
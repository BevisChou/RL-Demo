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

        self.eps = np.array([1e-5, 1e-5], dtype=np.float32)

        self.config = msg_pb2.Request.Config()
        self.config.g = 9.8
        self.config.k = 1
        self.config.m = 1
        self.config.l = 1
        self.config.w = 0.1

        self.context = zmq.Context()
        self.socket = self.context.socket(zmq.PAIR)
        self.socket.connect("tcp://127.0.0.1:5555")

    def step(self, action):
        request = msg_pb2.Request()
        request.type = msg_pb2.Request.RequestType.STEP
        request.action = action[0]
        self.socket.send(request.SerializeToString())

        message = self.socket.recv()
        response = msg_pb2.Response()
        response.ParseFromString(message)

        observation = np.array([response.state.angle, response.state.angular_velocity], dtype=np.float32)
        
        energy = self.calc_energy(observation)
        # reward = self.energy - energy
        reward = (self.energy - energy) / abs(observation[0])
        self.energy = energy

        done = False
        info = {
            "r": reward,
            "f": action[0],
            "a": observation[0],
            "av": observation[1]
        }

        if abs(observation[0]) > np.pi / 4:
            done = True
        elif (abs(observation) < self.eps).all():
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

        observation = np.array([response.state.angle, response.state.angular_velocity], dtype=np.float32)
        self.energy = self.calc_energy(observation)
        return observation

    def render(self, mode="human"):
        pass

    def close (self):
        request = msg_pb2.Request()
        request.type = msg_pb2.Request.RequestType.CLOSE
        self.socket.send(request.SerializeToString())

    def calc_energy (self, observation):
        return (1 - np.cos(observation[0])) * self.config.l * self.config.m * self.config.g + 0.5 * self.config.m * np.power(self.config.l * observation[1], 2)
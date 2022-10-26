from stable_baselines3.common.env_checker import check_env
from stable_baselines3 import SAC
from env import CustomEnv

print("CHECK ENV")
env = CustomEnv()
check_env(env)

print("TRAIN")
model = SAC("MlpPolicy", env, verbose=1)
model.learn(total_timesteps=1000)

print("ACT")
obs = env.reset()
while True:
    action, _states = model.predict(obs, deterministic=True)
    obs, reward, done, info = env.step(action)
    print(info) # debug
    env.render()
    if done:
        break
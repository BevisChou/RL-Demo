from stable_baselines3.common.env_checker import check_env
from stable_baselines3 import SAC
from env import CustomEnv

print("CHECK ENV")
env = CustomEnv()
check_env(env)

print("TRAIN")
model = SAC("MlpPolicy", env, verbose=1, tensorboard_log="./tensorboard_log/")
model.learn(total_timesteps=1_000_000, tb_log_name="sac")

print("ACT")
obs = env.reset(is_test=True)
while True:
    action, _states = model.predict(obs, deterministic=True)
    obs, reward, done, info = env.step(action)
    print(info) # debug
    env.render()
    if done:
        break
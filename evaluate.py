import gymnasium as gym
from stable_baselines3 import PPO
import time

# Load environment with rendering enabled
env = gym.make("CartPole-v1", render_mode="human")

# Load trained model
model = PPO.load("models/ppo_cartpole")

# Reset environment
obs, info = env.reset()

# Run evaluation loop
for episode in range(5):
    obs, info = env.reset()
    done = False
    total_reward = 0

    while not done:
        action, _states = model.predict(obs)

        obs, reward, terminated, truncated, info = env.step(action)

        done = terminated or truncated
        total_reward += reward

        env.render()
        time.sleep(0.01)

    print(f"Episode {episode + 1} reward: {total_reward}")

env.close()
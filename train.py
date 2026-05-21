import gymnasium as gym
from stable_baselines3 import PPO
from stable_baselines3.common.monitor import Monitor
import os

# Create folders if they do not exist
os.makedirs("models", exist_ok=True)
os.makedirs("videos", exist_ok=True)

# Create environment
env = gym.make("CartPole-v1")

# Monitor tracks rewards and statistics
env = Monitor(env)

# Create PPO model
model = PPO(
    "MlpPolicy",
    env,
    verbose=1,
    learning_rate=0.0003,
    n_steps=2048,
    batch_size=64,
)

# Train model
TIMESTEPS = 100000
model.learn(total_timesteps=TIMESTEPS)

# Save model
model.save("models/ppo_cartpole")

print("Training complete. Model saved.")
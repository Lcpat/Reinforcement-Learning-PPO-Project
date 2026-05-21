import matplotlib.pyplot as plt
import numpy as np

# Example placeholder data
# Replace later with real logged training data
episodes = np.arange(1, 11)
rewards = [20, 35, 50, 75, 120, 180, 250, 350, 450, 500]

plt.plot(episodes, rewards)
plt.xlabel("Training Stage")
plt.ylabel("Average Reward")
plt.title("CartPole PPO Training Performance")

plt.savefig("plots/training_curve.png")

plt.show()
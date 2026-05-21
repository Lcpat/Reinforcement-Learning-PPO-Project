# Reinforcement Learning PPO Project

> NOTE: WIP; THIS REPOSITORY IS CURRENTLY IN DEVELOPMENT

### Description:
A reinforcement learning (RL) study using Proximal Policy Optimization (PPO) to train an autonomous agent in the CartPole-v1 environment

### Goal:
Understand how reinforcement learning agents develop decision-making policies through reward optimization and environmental interaction

### Method:
- Implement PPO reinforcement learning agen
- Train autonomous balancing behavior and evaluate convergence/reward progression
- Analyze training stability across varying learning parameters and reward optimization
- Technologies used include: Python, Gymnasium, Stable-Baselines3, Matplotlib

### Progress:
- PPO training pipeline implemented
- Environment interaction configured
- Model saving/loading operational
- Evaluation and rendering system implemented
- Reward plotting functionality added

### Results:   
| Learning Rate (lr) | Time Steps | Average Reward (over 5 episodes) |
|---|---|---|
| 0.0003 | 100000 | **500** of 500 |
| 0.01 | 5000 | **122.2** of 500 |

### Next Steps:
- Compare PPO against additional RL algorithms
- Analyze hyperparameter sensitivity
- Add reward curve visualizations
- Record gameplay demonstrations

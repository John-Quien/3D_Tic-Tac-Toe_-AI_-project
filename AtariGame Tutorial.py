
"""Training the agent"""

import random
from IPython.display import clear_output
import gym
import numpy as np
env = gym.make("Taxi-v3").env

q_table = np.zeros([env.observation_space.n, env.action_space.n])

print("Action Space {}".format(env.action_space))  # we only have 6 movement options
print("State Space {}".format(env.observation_space))  # these are 500 possible states
# In this we need to map these states to give us some good learning
# we can call this a states and actions matrix/ reward table

print(env.P[328])
epochs = 0
penalties, reward = 0, 0

frames = []  # for animation

done = False

# Hyperparameters
alpha = 0.1
gamma = 0.6
epsilon = 0.1

# For plotting metrics
all_epochs = []
all_penalties = []

for i in range(1, 100001):
    state = env.reset()

    epochs, penalties, reward, = 0, 0, 0
    done = False

    while not done:
        if random.uniform(0, 1) < epsilon: # Return a random floating point number N such that a <= N <= b
            action = env.action_space.sample()  # Explore action space
        else:
            action = np.argmax(q_table[state])  # Exploit learned values

        next_state, reward, done, info = env.step(action)

        old_value = q_table[state, action]
        next_max = np.max(q_table[next_state])

        new_value = (1 - alpha) * old_value + alpha * (reward + gamma * next_max)
        q_table[state, action] = new_value

        if reward == -10:
            penalties += 1

        state = next_state
        epochs += 1

    if i % 100 == 0:
        clear_output(wait=True)
        print(f"Episode: {i}")

print("Training finished.\n")
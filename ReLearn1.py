import gym
import numpy as np

env = gym.make("MountainCar-v0") #environment has 3 actions you can take
# 0 = go left, 1 = no accel, 2 = go right
env.reset()
#resets the environment each time the program runs
# to the agent, it does not matter what these values represent
print(env.observation_space.high) #highest value for all the observations possible, state space
print(env.observation_space.low) #lowest value for all the observations possible
print(env.action_space.n) #how many actions you can take

DISCRETE_OS_SIZE = [20]*len(env.observation_space.high)
# the range between low value -1.2, -0.07 and high value 0.6, 0.07 will now be chunked into 20 buckets aka 20 discrete values instead
# of infinitely continous range that would take forever to create
discrete_os_win_size = (env.observation_space.high - env.observation_space.low)/DISCRETE_OS_SIZE
print(discrete_os_win_size)

q_table = np.random.uniform(low = -2, high = 0, size = (DISCRETE_OS_SIZE) + [env.action_space.n]) #rewards given, 20 by 20 table of discrete observations,
# contains every combo of observations we might find, every combo of position and velocity
# Now, need values for every single action possible
# [env.action.space.n] creates a 20 by 20 by 3 table, every combo of environment states, random q value in each of those cells
print(q_table.shape)
print(q_table)

done = False

while not done: #while True, allows us to step through the environment
    action = 2 #the car will always take the action of moving to the right
    new_state, reward, done, _ = env.step(action) #every time we step with an action, we get a new state (position and velocoty), a reward for that
    #action
    print(reward, new_state) #change continous values to discrete values (every possible combination to 8 decimal places is crazy)

    env.render()

env.close()

from __future__ import print_function
import gym
import sys
import random
import matplotlib.pyplot as plt

def Q(state, action):
    return states[state][action]

def epsilon_greedy_pick(state, epsilon): #picks direction with largest reward
    random_int = random.random()
    if random_int < epsilon:
        return random.randint(0, len(states[state])-1)
    else:
        action_index = 0
        for action_i in range(len(states[state])):
            if Q(state, action_index) < Q(state, action_i):
                action_index = action_i
        return action_index

def max_Q(state):
    action_index = 0
    for action_i in range(len(states[state])):
        if Q(state, action_index) < Q(state, action_i):
            action_index = action_i
    return states[state][action_index]

def Q_learning(state, action, next_state, next_action, reward):
    states[state][action] = states[state][action] + \
        learning_rate * \
            (reward + (disc_factor * states[next_state][next_action]) - \
                states[state][action])

env = gym.make('FrozenLake-v0')
epsilon = 0.1
learning_rate = 0.1
disc_factor = 0.99
states = []
for i in range(16):
    states.append([0.5, 1, 0.5, 0.5])

reward = 0
reward_list = []
episode = 1
while episode < 10000:
    state = env.reset()
    action = epsilon_greedy_pick(state, epsilon)
    for i in range(100):
        next_state, reward, done, info = env.step(action)
        next_action = epsilon_greedy_pick(next_state, epsilon)
        Q_learning(state, action, next_state, next_action, reward)
        action = next_action
        state = next_state
        if done:
            if reward == 1:
                reward_list.append(1)
            else:
                reward_list.append(0)
            break
    episode += 1

for state in states:
    print (state)
env.render()
plt.plot(reward_list)
plt.xlabel('Episode number')
plt.ylabel('Reward')
plt.show()
 # Assignment One train RL agent to navigate to cross the road with action right, left, right
import numpy as np

road_length = 5
start_pos  = 0
goal_pos = 4

actions = ['left', 'right']

# Q-table: rows=positions, columns=actions
Q = np.zeros((road_length, len(actions)))

# Hyperparameters
alpha = 0.1  # Learning rate
gamma = 0.9  # Discount factor
epsilon = 0.2  # Exploration rate
episodes = 200  # Number of episodes for training

for episode in range(episodes):
    state = start_pos
    done = False
    while not done:
        # Choose action (epsilon-greedy)
        if np.random.rand() < epsilon:
            action = np.random.choice([0, 1])
        else:
            action = np.argmax(Q[state])

        # Take action
        if actions[action] == 'right':
            next_state = min(state + 1, road_length - 1)
        else:
            next_state = max(state - 1, 0)

        # Reward
        if next_state == goal_pos:
            reward = 10
            done = True
        else:
            reward = -1

        # Q-learning update
        Q[state, action] = Q[state, action] + alpha * (
            reward + gamma * np.max(Q[next_state]) - Q[state, action]
        )

        state = next_state

state = start_pos
steps = []
while state != goal_pos:
    action = np.argmax(Q[state])
    steps.append(actions[action])
    if actions[action] == 'right':
        state = min(state + 1, road_length - 1)
    else:
        state = max(state - 1, 0)
        
print("Learned action sequence to cross the road:",steps)
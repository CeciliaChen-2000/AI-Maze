import numpy as np

from generate_maze import generate_maze


def policy_iteration(maze, gamma=0.99, epsilon=0.0001):
    rows, columns = len(maze), len(maze[0])

    actions = [[-1, 0], [1, 0], [0, -1], [0, 1]]  # up, down, left, right
    # set rewards to -1 for walls and -0.04 for every other cell
    # rewards = [[-100 if maze[r][c] == 1 else -0.00001 for c in range(columns)] for r in range(rows)]
    rewards = np.zeros((rows, columns))
    # set rewards to -1 for walls
    rewards[maze == 1] = -100
    # set rewards to -0.00001 for every other cell
    rewards[maze == 0] = -0.000000001

    V = np.zeros((rows, columns))
    # initialize the policy to a fixed action (up) in every state
    policy = [[0 for c in range(columns)] for r in range(rows)]

    while True:
        # policy evaluation
        # V = [[0 for c in range(columns)] for r in range(rows)]  # initialize all state values to 0
        while True:
            delta = 0
            for x in range(rows):
                for y in range(columns):
                    v = V[x][y]
                    if (x, y) == (1, 0):  # start state has a fixed value of 0
                        V[x][y] = 0
                    elif (x, y) == (rows - 2, columns - 1):  # goal state has a fixed value of 1
                        V[x][y] = 1
                    else:
                        action = policy[x][y]
                        next_x, next_y = x + actions[action][0], y + actions[action][1]
                        next_x = min(max(next_x, 0), rows - 1)
                        next_y = min(max(next_y, 0), columns - 1)
                        reward = rewards[next_x][next_y]
                        V[x][y] = reward + gamma * V[next_x][next_y]
                    delta = max(delta, abs(v - V[x][y]))
            if delta < epsilon:  # convergence
                break

        # policy improvement
        policy_stable = True
        for x in range(rows):
            for y in range(columns):
                if maze[x][y] == 1:  # wall
                    continue
                old_action = policy[x][y]

                # find the action that maximizes the expected future reward
                expected_rewards = []
                for action in actions:
                    next_x, next_y = x + action[0], y + action[1]
                    if next_x < 0 or next_x >= rows or next_y < 0 or next_y >= columns or maze[next_x][next_y] == 1:
                        # invalid move, stay in current state
                        expected_rewards.append(gamma * V[x][y])
                    else:
                        expected_reward = rewards[next_x][next_y] + gamma * V[next_x][next_y]
                        expected_rewards.append(expected_reward)
                new_action = expected_rewards.index(max(expected_rewards))
                policy[x][y] = new_action

                if old_action != new_action:
                    policy_stable = False
        if policy_stable:  # convergence
            print("convergence, finish value iteration")
            break
    # find optimal path using the final policy
    optimal_path = []
    x, y = (1, 1)
    while (x, y) != (rows - 2, columns - 2):
        action = policy[x][y]
        optimal_path.append([x, y])
        x, y = x + actions[action][0], y + actions[action][1]
    optimal_path.append([x, y])
    # convert policy actions from integers to letters
    for x in range(rows):
        for y in range(columns):
            if policy[x][y] == 0:
                policy[x][y] = 'U'
            elif policy[x][y] == 1:
                policy[x][y] = 'D'
            elif policy[x][y] == 2:
                policy[x][y] = 'L'
            elif policy[x][y] == 3:
                policy[x][y] = 'R'
    return policy, optimal_path


def get_PI_path(maze):
    policy, optimal_path = policy_iteration(maze)
    rows, columns = len(maze), len(maze[0])
    for x in range(rows):
        for y in range(columns):
            if maze[x][y] == 0:
                maze[x][y] = policy[x][y]
    print('MDP PI FINISHED')
    return maze, optimal_path


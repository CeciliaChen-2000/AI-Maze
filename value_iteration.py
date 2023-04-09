def value_iteration(maze, gamma=0.99, epsilon=0.0001):
    rows, columns = len(maze), len(maze[0])

    actions = [[-1, 0], [1, 0], [0, -1], [0, 1]]  # up, down, left, right
    # set rewards to -1 for walls and -0.04 for every other cell
    rewards = [[-100 if maze[r][c] == 1 else -0.000000001 for c in range(columns)] for r in range(rows)]

    V = [[0 for c in range(columns)] for r in range(rows)]  # initialize all state values to 0
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
                    # update state value by taking the maximum expected future reward
                    expected_rewards = []
                    for action in actions:
                        next_x, next_y = x + action[0], y + action[1]
                        if next_x < 0 or next_x >= rows or next_y < 0 or next_y >= columns or maze[next_x][next_y] == 1:
                            # invalid move, stay in current state
                            expected_rewards.append(gamma * V[x][y])
                        else:
                            expected_reward = rewards[next_x][next_y] + gamma * V[next_x][next_y]
                            expected_rewards.append(expected_reward)
                    V[x][y] = max(expected_rewards)
                delta = max(delta, abs(v - V[x][y]))
        if delta < epsilon:  # convergence
            break

    # find optimal policy using the state values
    optimal_policy = [[" " for c in range(columns)] for r in range(rows)]
    for x in range(rows):
        for y in range(columns):
            if maze[x][y] == 1:  # wall
                optimal_policy[x][y] = "#"
            else:
                max_value, max_action = -float("inf"), None
                for index, action in enumerate(actions):
                    next_x, next_y = x + action[0], y + action[1]
                    if 0 <= next_x < rows and 0 <= next_y < columns and maze[next_x][next_y] == 0:
                        if V[next_x][next_y] > max_value:
                            max_value = V[next_x][next_y]
                            max_action = index
                optimal_policy[x][y] = max_action
    # find optimal path using the final policy
    optimal_path = []
    x, y = (1, 1)
    while (x, y) != (rows - 2, columns - 2):
        action = optimal_policy[x][y]
        optimal_path.append([x, y])
        x, y = x + actions[action][0], y + actions[action][1]
    optimal_path.append([x, y])

    # convert policy actions from integers to letters
    for x in range(rows):
        for y in range(columns):
            if optimal_policy[x][y] == 0:
                optimal_policy[x][y] = 'U'
            elif optimal_policy[x][y] == 1:
                optimal_policy[x][y] = 'D'
            elif optimal_policy[x][y] == 2:
                optimal_policy[x][y] = 'L'
            elif optimal_policy[x][y] == 3:
                optimal_policy[x][y] = 'R'
    return optimal_policy, optimal_path


def get_VI_path(maze):
    policy, optimal_path = value_iteration(maze)

    rows, columns = len(maze), len(maze[0])
    start_pos = (1, 1)
    end_pos = (rows - 2, columns - 2)
    for x in range(rows):
        for y in range(columns):
            if policy[x][y] == 'U' or policy[x][y] == 'D' or policy[x][y] == 'R' or policy[x][y] == 'L':
                maze[x][y] = policy[x][y]
    print('MDP VI FINISHED')
    return maze, optimal_path

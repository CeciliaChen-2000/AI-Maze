def dfs(maze):
    rows, columns = len(maze), len(maze[0])
    start_pos = (1, 1)
    end_pos = (rows - 2, columns - 2)

    stack = [start_pos]
    while stack:
        cur_pos = stack[-1]
        if cur_pos == end_pos:
            print("DFS FINISHED")
            return stack
        x, y = cur_pos
        maze[x][y] = 2  # 记录走过的点
        if maze[x - 1][y] == 0:
            stack.append((x - 1, y))
            continue
        elif maze[x][y + 1] == 0:
            stack.append((x, y + 1))
            continue
        elif maze[x + 1][y] == 0:
            stack.append((x + 1, y))
            continue
        elif maze[x][y - 1] == 0:
            stack.append((x, y - 1))
            continue
        else:  # 走不通过，直接循环干掉每一步，重新调整路线
            stack.pop()

    print("NO EXIT")
    return False

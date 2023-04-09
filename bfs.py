from collections import deque


def bfs(maze):
    rows, columns = len(maze), len(maze[0])
    start_pos = (1, 1)
    end_pos = (rows - 2, columns - 2)

    dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    queue = deque([start_pos])
    predecessors = {start_pos: None}

    while queue:
        cur_pos = queue.popleft()  # remove and return the leftmost element
        if cur_pos == end_pos:
            print("BFS FINISHED")
            path = []
            while cur_pos:
                path.append(cur_pos)
                cur_pos = predecessors[cur_pos]
            return list(reversed(path))

        x, y = cur_pos
        for dx, dy in dirs:
            next_x, next_y = x + dx, y + dy
            if 0 < next_x < rows and 0 < next_y < columns and maze[next_x][next_y] == 0 and (
                    next_x, next_y) not in predecessors:
                queue.append((next_x, next_y))
                predecessors[(next_x, next_y)] = cur_pos
                maze[next_x][next_y] = 2  # record the walked path

    print("NO EXIT")
    return False

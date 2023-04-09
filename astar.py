from queue import PriorityQueue


def astar(maze):
    rows, columns = len(maze), len(maze[0])
    start_pos = (1, 1)
    end_pos = (rows - 2, columns - 2)

    dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    queue = PriorityQueue()
    queue.put((0, start_pos))
    predecessors = {start_pos: None}
    g_values = {start_pos: 0}

    def heuristic(a, b):
        # return ((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2) ** 0.5  # calculate the Euclidian Distance
        return abs(b[0] - a[0]) + abs(b[1] - a[1])  # calculate the Manhattan Distance

    while not queue.empty():
        _, cur_pos = queue.get()
        if cur_pos == end_pos:
            print("A* FINISHED")
            path = []
            while cur_pos:
                path.append(cur_pos)
                cur_pos = predecessors[cur_pos]
            return list(reversed(path))

        x, y = cur_pos
        for dx, dy in dirs:
            next_x, next_y = x + dx, y + dy
            if 0 < next_x < rows and 0 < next_y < columns and maze[next_x][next_y] == 0:
                new_g_value = g_values[cur_pos] + 1
                if (next_x, next_y) not in g_values or new_g_value < g_values[(next_x, next_y)]:
                    g_values[(next_x, next_y)] = new_g_value
                    priority = new_g_value + heuristic(end_pos, (next_x, next_y))
                    queue.put((priority, (next_x, next_y)))
                    predecessors[(next_x, next_y)] = cur_pos
                    maze[next_x][next_y] = 2

    print("NO EXIT")
    return False

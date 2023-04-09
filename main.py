import copy
import datetime
import time

from astar import astar
from bfs import bfs
from dfs import dfs
from generate_maze import generate_maze, print_maze, show_maze
from value_iteration import value_iteration, get_VI_path
from policy_iteration import policy_iteration, get_PI_path


cell_size = int(input("Cell size: "))
rows = int(input("Rows of maze: "))
columns = int(input("Columns of maze: "))


a_maze = generate_maze(rows, columns)
print_maze(a_maze)
show_maze(a_maze, 'Maze', cell_size)

dfs_maze = copy.deepcopy(a_maze)
start_time = datetime.datetime.now()
dfs_path = dfs(dfs_maze)
end_time = datetime.datetime.now()
print(f"DFS {end_time - start_time} sec.")
for pos in dfs_path:
    dfs_maze[pos[0]][pos[1]] = -1
show_maze(dfs_maze, 'DFS', cell_size)
# show_path(dfs_maze, dfs_path)

bfs_maze = copy.deepcopy(a_maze)
start_time = datetime.datetime.now()
bfs_path = bfs(bfs_maze)
end_time = datetime.datetime.now()
print(f"BFS {end_time - start_time} sec.")
for pos in bfs_path:
    bfs_maze[pos[0]][pos[1]] = -1
show_maze(bfs_maze, 'BFS', cell_size)

astar_maze = copy.deepcopy(a_maze)
start_time = datetime.datetime.now()
astar_path = astar(astar_maze)
end_time = datetime.datetime.now()
print(f"A* {end_time - start_time} sec.")
for pos in astar_path:
    astar_maze[pos[0]][pos[1]] = -1
show_maze(astar_maze, 'A*', cell_size)


VI_maze = copy.deepcopy(a_maze)
start_time = datetime.datetime.now()
VI_maze, VI_path = get_VI_path(VI_maze)
end_time = datetime.datetime.now()
print(f"MDP VI {end_time - start_time} sec.")
for pos in VI_path:
    VI_maze[pos[0]][pos[1]] = -1
show_maze(VI_maze, 'MDP VI', cell_size)

PI_maze = copy.deepcopy(a_maze)
start_time = datetime.datetime.now()
PI_maze, PI_path = get_PI_path(PI_maze)
end_time = datetime.datetime.now()
print(f"MDP PI {end_time - start_time} sec.")
for pos in PI_path:
    PI_maze[pos[0]][pos[1]] = -1
show_maze(PI_maze, 'MDP PI', cell_size)

import os
import random
import sys
import pygame

sys.setrecursionlimit(10000)  # 修改递归深度限制为10000


# Reference: https://github.com/joewing/maze/blob/master/maze.py
def generate_maze(rows, columns):
    # The size of the maze should be odd
    maze = [[1 for c in range(columns)] for r in range(rows)]  # initialize the maze

    random.seed()
    maze[1][1] = 0  # start

    def carve_maze(x, y):
        direction = random.randint(0, 3)
        count = 0
        while count < 4:
            dx, dy = 0, 0
            if direction == 0:  # down
                dx = 1
            elif direction == 1:  # right
                dy = 1
            elif direction == 2:  # up
                dx = -1
            else:  # left
                dy = -1
            x1, y1 = x + dx, y + dy
            x2, y2 = x1 + dx, y1 + dy
            if 0 < x2 < len(maze) and 0 < y2 < len(maze[0]):  # In the range of maze
                if maze[x1][y1] == 1 and maze[x2][y2] == 1:
                    maze[x1][y1] = 0
                    maze[x2][y2] = 0
                    carve_maze(x2, y2)
            count = count + 1
            direction = (direction + 1) % 4

    carve_maze(1, 1)
    maze[1][0] = 0  # entrance
    maze[rows - 2][columns - 1] = 0  # exit
    return maze


def print_maze(maze):
    for x in range(0, len(maze)):
        for y in range(0, len(maze[0])):
            if maze[x][y] == 1:
                sys.stdout.write("[]")
            else:
                sys.stdout.write("  ")
        sys.stdout.write("\n")


def show_maze(maze, title, cell_size):
    WALL = (0, 0, 0)
    ROAD = (255, 255, 255)
    PATH = (200, 0, 0)
    ARROW = (100, 100, 100)
    # initialize pygame window
    pygame.init()
    window_size = (len(maze[0]) * cell_size, len(maze) * cell_size)
    screen = pygame.display.set_mode(window_size)
    pygame.display.set_caption(f"{title} - {len(maze)}×{len(maze[0])}")

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((255, 255, 255))
        for x in range(len(maze)):
            for y in range(len(maze[0])):
                if maze[x][y] == 1:  # wall
                    pygame.draw.rect(screen, WALL, (y * cell_size, x * cell_size, cell_size, cell_size))
                elif maze[x][y] == -1:  # path
                    pygame.draw.rect(screen, PATH, (y * cell_size, x * cell_size, cell_size, cell_size))
                elif maze[x][y] == 2:  # 走过的点
                    pygame.draw.rect(screen, (150, 150, 150), (y * cell_size, x * cell_size, cell_size, cell_size))

                elif maze[x][y] == 'D':  # arrow down
                    font = pygame.font.SysFont(name='Down', size=cell_size)
                    text = font.render("v", True, ARROW)
                    text_rect = text.get_rect(center=(y * cell_size + cell_size / 2, x * cell_size + cell_size / 2))
                    screen.blit(text, text_rect)
                elif maze[x][y] == 'U':  # arrow up
                    font = pygame.font.SysFont(name='Up', size=cell_size)
                    text = font.render("^", True, ARROW)
                    text_rect = text.get_rect(center=(y * cell_size + cell_size / 2, x * cell_size + cell_size / 2))
                    screen.blit(text, text_rect)
                elif maze[x][y] == 'R':  # arrow right
                    font = pygame.font.SysFont(name='Right', size=cell_size)
                    text = font.render(">", True, ARROW)
                    text_rect = text.get_rect(center=(y * cell_size + cell_size / 2, x * cell_size + cell_size / 2))
                    screen.blit(text, text_rect)
                elif maze[x][y] == 'L':  # arrow left
                    font = pygame.font.SysFont(name='Left', size=cell_size)
                    text = font.render("<", True, ARROW)
                    text_rect = text.get_rect(center=(y * cell_size + cell_size / 2, x * cell_size + cell_size / 2))
                    screen.blit(text, text_rect)

                else:  # road
                    pygame.draw.rect(screen, ROAD, (y * cell_size, x * cell_size, cell_size, cell_size))
        pygame.display.flip()

    # save the image
    save_path = os.path.abspath('./maze_images')
    version = 1
    while True:
        try:
            open("{}/{}×{}Maze{}.png".format(save_path, len(maze), len(maze[0]), version), "r")
        except:
            break
        version += 1
    pygame.image.save(screen, "{}/{}×{}Maze{}.png".format(save_path, len(maze), len(maze[0]), version))
    pygame.quit()


def show_path(maze, path):
    for i, p in enumerate(path):
        if i == 0:
            maze[p[0]][p[1]] = "S"
        elif i == len(path) - 1:
            maze[p[0]][p[1]] = "E"
        else:
            maze[p[0]][p[1]] = 3
    print("\n")
    for r in maze:
        for c in r:
            if c == 3:
                print('\033[0;31m' + "*" + " " + '\033[0m', end="")
            elif c == "S" or c == "E":
                print('\033[0;34m' + c + " " + '\033[0m', end="")
            elif c == 2:
                print('\033[0;32m' + "#" + " " + '\033[0m', end="")
            elif c == 1:
                print('\033[0;;40m' + " " * 2 + '\033[0m', end="")
            else:
                print(" " * 2, end="")
        print()
    return

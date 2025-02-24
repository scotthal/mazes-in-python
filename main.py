from maze.maze import Maze
from maze_algorithm.binary_tree import binary_tree
from maze_render.svg import svg

def main():
    maze_width = 30
    maze_height = 30
    cell_width = 20
    cell_height = 20
    maze = Maze(maze_width, maze_height)
    binary_tree(maze)
    svg(maze, cell_width, cell_height)

if __name__ == "__main__":
    main()


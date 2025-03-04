from maze.maze import Maze
from maze_algorithm.sidewinder import sidewinder
from maze_render.svg import svg_distance

def main():
    maze_width = 30
    maze_height = 30
    cell_width = 20
    cell_height = 20
    maze = Maze(maze_width, maze_height)
    sidewinder(maze)
    svg_distance(maze, cell_width, cell_height)

if __name__ == "__main__":
    main()


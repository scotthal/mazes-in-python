import random

def binary_tree(maze):
    random.seed()
    for coordinate in [(x, y) for y in range(maze.height) for x in range(maze.width)]:
        neighbors = maze.neighbors[maze.linearize(coordinate)]
        if 'north' in neighbors and 'east' in neighbors:
            if random.random() > 0.5:
                maze.link(coordinate, neighbors['north'])
            else:
                maze.link(coordinate, neighbors['east'])
        elif 'north' in neighbors:
            maze.link(coordinate, neighbors['north'])
        elif 'east' in neighbors:
            maze.link(coordinate, neighbors['east'])


import random


def close_run(maze, run):
    coordinate = random.choice(run)
    neighbors = maze.neighbors[maze.linearize(coordinate)]
    if 'north' in neighbors:
        maze.link(coordinate, neighbors['north'])
    run.clear()


def sidewinder(maze):
    random.seed()
    run = []
    for coordinate in [(x, y) for y in range(maze.height)
                       for x in range(maze.width)]:
        run.append(coordinate)
        neighbors = maze.neighbors[maze.linearize(coordinate)]
        if 'north' in neighbors and 'east' in neighbors:
            if random.random() > 0.5:
                maze.link(coordinate, neighbors['east'])
            else:
                close_run(maze, run)
        elif 'north' in neighbors:
            close_run(maze, run)
        elif 'east' in neighbors:
            maze.link(coordinate, neighbors['east'])

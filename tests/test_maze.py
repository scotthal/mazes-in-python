import unittest
from maze.maze import Maze


class TestMaze(unittest.TestCase):

    def test_basic_maze(self):
        maze = Maze(3, 3)
        self.assertEqual(maze.width, 3)
        self.assertEqual(maze.height, 3)
        self.assertEqual(maze.linearize((0, 0)), 0)

        coordinate = (0, 0)
        self.assertEqual(len(maze.neighbors[maze.linearize(coordinate)]), 2)
        self.assertEqual(maze.neighbors[maze.linearize(coordinate)]['north'],
                         (0, 1))
        self.assertEqual(maze.neighbors[maze.linearize(coordinate)]['east'],
                         (1, 0))
        self.assertEqual(len(maze.links[maze.linearize(coordinate)]), 0)

        coordinate = (1, 0)
        self.assertEqual(len(maze.neighbors[maze.linearize(coordinate)]), 3)
        self.assertEqual(maze.neighbors[maze.linearize(coordinate)]['north'],
                         (1, 1))
        self.assertEqual(maze.neighbors[maze.linearize(coordinate)]['east'],
                         (2, 0))
        self.assertEqual(maze.neighbors[maze.linearize(coordinate)]['west'],
                         (0, 0))
        self.assertEqual(len(maze.links[maze.linearize(coordinate)]), 0)

        coordinate = (2, 0)
        self.assertEqual(len(maze.neighbors[maze.linearize(coordinate)]), 2)
        self.assertEqual(maze.neighbors[maze.linearize(coordinate)]['north'],
                         (2, 1))
        self.assertEqual(maze.neighbors[maze.linearize(coordinate)]['west'],
                         (1, 0))
        self.assertEqual(len(maze.links[maze.linearize(coordinate)]), 0)

        coordinate = (0, 1)
        self.assertEqual(len(maze.neighbors[maze.linearize(coordinate)]), 3)
        self.assertEqual(maze.neighbors[maze.linearize(coordinate)]['north'],
                         (0, 2))
        self.assertEqual(maze.neighbors[maze.linearize(coordinate)]['east'],
                         (1, 1))
        self.assertEqual(maze.neighbors[maze.linearize(coordinate)]['south'],
                         (0, 0))
        self.assertEqual(len(maze.links[maze.linearize(coordinate)]), 0)

        coordinate = (1, 1)
        self.assertEqual(len(maze.neighbors[maze.linearize(coordinate)]), 4)
        self.assertEqual(maze.neighbors[maze.linearize(coordinate)]['north'],
                         (1, 2))
        self.assertEqual(maze.neighbors[maze.linearize(coordinate)]['east'],
                         (2, 1))
        self.assertEqual(maze.neighbors[maze.linearize(coordinate)]['south'],
                         (1, 0))
        self.assertEqual(maze.neighbors[maze.linearize(coordinate)]['west'],
                         (0, 1))
        self.assertEqual(len(maze.links[maze.linearize(coordinate)]), 0)

        coordinate = (2, 1)
        self.assertEqual(len(maze.neighbors[maze.linearize(coordinate)]), 3)
        self.assertEqual(maze.neighbors[maze.linearize(coordinate)]['north'],
                         (2, 2))
        self.assertEqual(maze.neighbors[maze.linearize(coordinate)]['south'],
                         (2, 0))
        self.assertEqual(maze.neighbors[maze.linearize(coordinate)]['west'],
                         (1, 1))
        self.assertEqual(len(maze.links[maze.linearize(coordinate)]), 0)

        coordinate = (0, 2)
        self.assertEqual(len(maze.neighbors[maze.linearize(coordinate)]), 2)
        self.assertEqual(maze.neighbors[maze.linearize(coordinate)]['south'],
                         (0, 1))
        self.assertEqual(maze.neighbors[maze.linearize(coordinate)]['east'],
                         (1, 2))
        self.assertEqual(len(maze.links[maze.linearize(coordinate)]), 0)

        coordinate = (1, 2)
        self.assertEqual(len(maze.neighbors[maze.linearize(coordinate)]), 3)
        self.assertEqual(maze.neighbors[maze.linearize(coordinate)]['south'],
                         (1, 1))
        self.assertEqual(maze.neighbors[maze.linearize(coordinate)]['west'],
                         (0, 2))
        self.assertEqual(maze.neighbors[maze.linearize(coordinate)]['east'],
                         (2, 2))
        self.assertEqual(len(maze.links[maze.linearize(coordinate)]), 0)

        coordinate = (2, 2)
        self.assertEqual(len(maze.neighbors[maze.linearize(coordinate)]), 2)
        self.assertEqual(maze.neighbors[maze.linearize(coordinate)]['south'],
                         (2, 1))
        self.assertEqual(maze.neighbors[maze.linearize(coordinate)]['west'],
                         (1, 2))
        self.assertEqual(len(maze.links[maze.linearize(coordinate)]), 0)

    def test_simple_link(self):
        maze = Maze(2, 2)
        self.assertEqual(len(maze.links[maze.linearize((0, 0))]), 0)
        maze.link((0, 0), (1, 0))

        coordinate = (0, 0)
        self.assertEqual(len(maze.links[maze.linearize(coordinate)]), 1)
        self.assertEqual(maze.links[maze.linearize(coordinate)]['east'],
                         (1, 0))

        maze.link((1, 0), (1, 1))
        coordinate = (1, 0)
        self.assertEqual(len(maze.links[maze.linearize(coordinate)]), 2)
        self.assertEqual(maze.links[maze.linearize(coordinate)]['west'],
                         (0, 0))
        self.assertEqual(maze.links[maze.linearize(coordinate)]['north'],
                         (1, 1))

        maze.link((1, 1), (0, 1))
        coordinate = (1, 1)
        self.assertEqual(len(maze.links[maze.linearize(coordinate)]), 2)
        self.assertEqual(maze.links[maze.linearize(coordinate)]['west'],
                         (0, 1))
        self.assertEqual(maze.links[maze.linearize(coordinate)]['south'],
                         (1, 0))

    def test_calculate_distances(self):
        maze = Maze(2, 2)
        maze.link((0, 0), (1, 0))
        maze.link((1, 0), (1, 1))
        maze.link((1, 1), (0, 1))

        maze.calculate_distances((0, 0))
        distances = maze.distances[maze.linearize((0, 0))]
        self.assertEqual(distances[maze.linearize((0, 0))], 0)
        self.assertEqual(distances[maze.linearize((1, 0))], 1)
        self.assertEqual(distances[maze.linearize((1, 1))], 2)
        self.assertEqual(distances[maze.linearize((0, 1))], 3)

    def test_shortest_path(self):
        maze = Maze(2, 2)
        maze.link((0, 0), (1, 0))
        maze.link((1, 0), (1, 1))
        maze.link((1, 1), (0, 1))

        path = maze.shortest_path((0, 0), (0, 1))
        self.assertEqual(len(path), 4)
        self.assertEqual(path[0], (0, 1))
        self.assertEqual(path[1], (1, 1))
        self.assertEqual(path[2], (1, 0))
        self.assertEqual(path[3], (0, 0))


if __name__ == "__main__":
    unittest.main()

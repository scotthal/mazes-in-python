from collections import deque
import math


class Maze:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.neighbors = []
        self.links = []
        self.distances = []
        for y in range(self.height):
            for x in range(self.width):
                neighbors = {}
                links = {}
                distances = []
                if (y < height - 1):
                    neighbors['north'] = (x, y + 1)
                if (x < width - 1):
                    neighbors['east'] = (x + 1, y)
                if (y > 0):
                    neighbors['south'] = (x, y - 1)
                if (x > 0):
                    neighbors['west'] = (x - 1, y)

                self.neighbors.append(neighbors)
                self.links.append(links)
                self.distances.append(distances)

    def linearize(self, coordinate):
        return (coordinate[1] * self.width) + coordinate[0]

    def delinearize(self, index):
        return ((index % self.width), math.floor(index / self.width))

    def link(self, coordinate1, coordinate2):
        index1 = self.linearize(coordinate1)
        index2 = self.linearize(coordinate2)
        neighbors1 = self.neighbors[index1]
        if 'east' in neighbors1 and neighbors1['east'] == coordinate2:
            self.links[index1]['east'] = coordinate2
            self.links[index2]['west'] = coordinate1
        elif 'north' in neighbors1 and neighbors1['north'] == coordinate2:
            self.links[index1]['north'] = coordinate2
            self.links[index2]['south'] = coordinate1
        elif 'south' in neighbors1 and neighbors1['south'] == coordinate2:
            self.links[index1]['south'] = coordinate2
            self.links[index2]['north'] = coordinate1
        elif 'west' in neighbors1 and neighbors1['west'] == coordinate2:
            self.links[index1]['west'] = coordinate2
            self.links[index2]['east'] = coordinate1

    def calculate_distances(self, coordinate):
        if len(self.distances[self.linearize(coordinate)]) > 0:
            return

        distances = [-1] * (self.width * self.height)
        distances[self.linearize(coordinate)] = 0
        frontier = deque()
        frontier.append(coordinate)

        while len(frontier) > 0:
            current_index = self.linearize(frontier[0])
            current_distance = distances[current_index]
            for link in self.links[current_index].values():
                if distances[self.linearize(link)] == -1:
                    distances[self.linearize(link)] = current_distance + 1
                    frontier.append(link)
            frontier.popleft()

        self.distances[self.linearize(coordinate)] = distances

    def shortest_path(self, from_coordinate, to_coordinate):
        self.calculate_distances(from_coordinate)
        distances = self.distances[self.linearize(from_coordinate)]
        path = []
        path.append(to_coordinate)
        current_coordinate = to_coordinate
        while current_coordinate != from_coordinate:
            current_distance = distances[self.linearize(current_coordinate)]
            for link in self.links[self.linearize(
                    current_coordinate)].values():
                if distances[self.linearize(link)] == current_distance - 1:
                    next_coordinate = link
                    break
            path.append(next_coordinate)
            current_coordinate = next_coordinate

        return path

    def longest_path(self):
        self.calculate_distances((0, 0))
        distances = self.distances[self.linearize((0, 0))]
        maximum_distance = max(distances)
        farthest_coordinate1 = self.delinearize(
            distances.index(maximum_distance))
        self.calculate_distances(farthest_coordinate1)
        distances = self.distances[self.linearize(farthest_coordinate1)]
        maximum_distance = max(distances)
        farthest_coordinate2 = self.delinearize(distances.index(maximum_distance))
        return self.shortest_path(farthest_coordinate1, farthest_coordinate2)


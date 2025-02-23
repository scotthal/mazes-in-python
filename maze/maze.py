class Maze:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.neighbors = []
        self.links = []
        for y in range(self.height):
            for x in range(self.width):
                neighbors = {}
                links = {}
                if (y < height - 1):
                    neighbors['north'] = (x, y + 1)
                if (x < width - 1):
                    neighbors['east'] = (x + 1, y)
                if (y > 0):
                    neighbors['south'] = (x, y - 1)
                if (x > 0):
                    neighbors['west'] = (x -1 , y)

                self.neighbors.append(neighbors)
                self.links.append(links)

    def linearize(self, coordinate):
        return (coordinate[1] * self.width) + coordinate[0]

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


from maze.maze import Maze
import math


def svg_open(maze, cell_width, cell_height):
    print('<svg version="1.1" ', end='')
    print(f'width="{maze.width * cell_width}" ', end='')
    print(f'height="{maze.height * cell_height}" ', end='')
    print('xmlns="http://www.w3.org/2000/svg" ', end='')
    print('>')


def svg_close():
    print('</svg>')


def background(background_color):
    print(f'<rect width="100%" height="100%" fill="{background_color}" />')


def line(maze, stroke, stroke_width, x1, y1, x2, y2):
    print(f'<line stroke="{stroke}" stroke_width="{stroke_width}" ', end='')
    print(f'x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" ', end='')
    print('/>')


def fill_rectangle(maze, fill_color, x, y, width, height):
    print(f'<rect fill="{fill_color}" ', end='')
    print(f'x="{x}" y="{y}" width="{width}" height="{height}" ', end='')
    print('/>')


def render_cell(maze, cell_width, cell_height, stroke, stroke_width,
                coordinate):
    if 'east' not in maze.links[maze.linearize(coordinate)]:
        line(maze, stroke, stroke_width,
             (coordinate[0] * cell_width) + cell_width,
             (coordinate[1] * cell_height) + cell_height,
             (coordinate[0] * cell_width) + cell_width,
             coordinate[1] * cell_height)
    if 'north' not in maze.links[maze.linearize(coordinate)]:
        line(
            maze,
            stroke,
            stroke_width,
            coordinate[0] * cell_width,
            (coordinate[1] * cell_height) + cell_height,
            (coordinate[0] * cell_width) + cell_width,
            (coordinate[1] * cell_height) + cell_height,
        )
    if 'south' not in maze.links[maze.linearize(coordinate)]:
        line(maze, stroke, stroke_width, coordinate[0] * cell_width,
             coordinate[1] * cell_height,
             (coordinate[0] * cell_width) + cell_width,
             coordinate[1] * cell_height)
    if 'west' not in maze.links[maze.linearize(coordinate)]:
        line(maze, stroke, stroke_width, coordinate[0] * cell_width,
             (coordinate[1] * cell_height) + cell_height,
             coordinate[0] * cell_width, coordinate[1] * cell_height)


def svg(maze, cell_width, cell_height):
    svg_open(maze, cell_width, cell_height)
    background('white')
    for coordinate in [(x, y) for y in range(maze.height)
                       for x in range(maze.width)]:
        render_cell(maze, cell_width, cell_height, "black", "1", coordinate)
    svg_close()


def distance_color(distance, maximum_distance):
    intensity = (maximum_distance - distance) / maximum_distance
    dark = math.floor(255 * intensity)
    bright = math.floor(128 + (127 * intensity))
    return f'rgb({dark}, {bright}, {dark})'


def svg_distance(maze, cell_width, cell_height):
    center = (math.floor(maze.width / 2), math.floor(maze.height / 2))
    maze.calculate_distances(center)
    distances = maze.distances[maze.linearize(center)]
    maximum_distance = max(distances)
    svg_open(maze, cell_width, cell_height)
    for coordinate in [(x, y) for y in range(maze.height)
                       for x in range(maze.width)]:
        distance = distances[maze.linearize(coordinate)]
        fill_color = distance_color(distance, maximum_distance)
        x = coordinate[0] * cell_width
        y = coordinate[1] * cell_height
        fill_rectangle(maze, fill_color, x, y, cell_width, cell_height)
        render_cell(maze, cell_width, cell_height, "black", "1", coordinate)
    svg_close()

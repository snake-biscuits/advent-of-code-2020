import math


with open("directions.txt") as file:
    directions = [(line[0], int(line[1:])) for line in file]


def rotate_clockwise(x, y, degrees):
    theta = math.radians(degrees)
    cos_theta = math.cos(theta)
    sin_theta = math.sin(theta)
    out_x = round(math.fsum([x * cos_theta, y * sin_theta]), 6)
    out_y = round(math.fsum([-x * sin_theta, y * cos_theta]), 6)
    return out_x, out_y


x, y = 0, 0  # start
cardinal = {"N": (0, 1), "S": (0, -1), "E": (1, 0), "W": (-1, 0)}
direction = cardinal["E"]
for approach, units in directions:
    if approach in cardinal:
        x, y = [a + (b * units) for a, b in zip((x, y), cardinal[approach])]
    elif approach in "LR":
        degrees = (units if approach == "R" else -units)
        direction = rotate_clockwise(*direction, degrees)
    elif approach == "F":
        x, y = [a + (b * units) for a, b in zip((x, y), direction)]

print(f"Manhattan distance from start is {abs(x) + abs(y)}")

import collections


with open("ferry.txt") as file:
    ferry = [line.rstrip("\n") for line in file]

width = len(ferry[0]) - 1
height = len(ferry) - 1


def first_visible(start, direction):
    x, y = start
    dir_x, dir_y = direction
    space = "."
    while space == ".":
        x += dir_x
        y += dir_y
        if any((x < 0, y < 0, x > width, y > height)):
            return None
        space = ferry[y][x]
    return x, y


directions = ((-1, -1), (0, -1), (1, -1),
              (-1,  0),          (1,  0),
              (-1,  1), (0,  1), (1,  1))

neighbours = collections.defaultdict(set)
for y, row in enumerate(ferry):
    for x, space in enumerate(row):
        if space == ".":
            continue
        for seat in [first_visible((x, y), d) for d in directions]:
            if seat is not None:
                neighbours[(x, y)].add(seat)

this_turn = {(x, y): ferry[y][x] for x, y in neighbours}
previous_turn = None
while this_turn != previous_turn:
    previous_turn = this_turn.copy()
    for seat, occupancy in previous_turn.items():
        ns = [previous_turn[(x, y)] for x, y in neighbours[seat]]
        if occupancy == "#" and ns.count("#") >= 5:
            this_turn[seat] = "L"
        elif occupancy == "L" and ns.count("#") == 0:
            this_turn[seat] = "#"
        else:
            this_turn[seat] = occupancy

print(f"{''.join(this_turn.values()).count('#')} seats filled")

import itertools


universe = set()
with open("cubes.txt") as file:
    x, y = 0, 0
    for line in file:
        line = line.rstrip("\n")
        cubes = {(x, y, 0) for x, char in enumerate(line) if char == "#"}
        universe = universe | cubes
        y += 1


def neighbours(cube):
    x, y, z = cube
    for a in (x - 1, x, x + 1):
        for b in (y - 1, y, y + 1):
            for c in (z - 1, z, z + 1):
                if (a, b, c) == (x, y, z):
                    continue
                yield a, b, c


def update(universe):
    next_universe = set()
    to_check = universe | set(itertools.chain(*map(neighbours, universe)))
    for cube in to_check:
        active_ns = sum(c in universe for c in neighbours(cube))
        if cube in universe:  # active
            if active_ns == 2 or active_ns == 3:
                next_universe.add(cube)
        else:
            if active_ns == 3:
                next_universe.add(cube)
    return next_universe


def visualise(universe):
    xs, ys, zs = set(), set(), set()
    for x, y, z in universe:
        xs.add(x)
        ys.add(y)
        zs.add(z)
    for z in range(min(zs), max(zs) + 1):
        print(f"{z=}")
        for y in range(min(ys), max(ys) + 1):
            for x in range(min(xs), max(xs) + 1):
                print("#" if (x, y, z) in universe else ".", end="")
            print()
        print()


# print(f"=== TICK 0 ===")
# visualise(universe)
for i in range(6):
    universe = update(universe)
    # print(f"=== TICK {i + 1:02} ===")
    # visualise(universe)

print(f"{len(universe)} cubes in active state after 6 cycles")  # 286

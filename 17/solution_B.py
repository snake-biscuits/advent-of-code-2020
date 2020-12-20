import itertools


universe = set()
with open("cubes.txt") as file:
    x, y = 0, 0
    for line in file:
        line = line.rstrip("\n")
        cubes = {(x, y, 0, 0) for x, char in enumerate(line) if char == "#"}
        universe = universe | cubes
        y += 1


def neighbours(cube):
    x, y, z, w = cube
    for a in (x - 1, x, x + 1):
        for b in (y - 1, y, y + 1):
            for c in (z - 1, z, z + 1):
                for d in (w - 1, w, w + 1):
                    if (a, b, c, d) == (x, y, z, w):
                        continue
                    yield a, b, c, d


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
    xs, ys, zs, ws = set(), set(), set(), set()
    for x, y, z, w in universe:
        xs.add(x)
        ys.add(y)
        zs.add(z)
        ws.add(w)
    for w in range(min(ws), max(ws) + 1):
        for z in range(min(zs), max(zs) + 1):
            print(f"{z=}, {w=}")
            for y in range(min(ys), max(ys) + 1):
                for x in range(min(xs), max(xs) + 1):
                    print("#" if (x, y, z) in universe else ".", end="")
                print()
            print()
        print()


# print(f"=== TICK 0 ===")
# visualise(universe)
for i in range(6):
    universe = update(universe)
    # print(f"=== TICK {i + 1:02} ===")
    # visualise(universe)

print(f"{len(universe)} cubes in active state after 6 cycles")  # 960

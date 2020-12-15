with open("ferry.txt") as file:
    ferry = [line.rstrip("\n") for line in file]

height = len(ferry[0]) - 1
width = len(ferry) - 1


def neighbours(x, y):
    xs = {x - 1 if x > 0 else x, x, x + 1 if x < width else x}
    ys = {y - 1 if y > 0 else y, y, y + 1 if y < height else y}
    out = set()
    for i in xs:
        for j in ys:
            out.add((i, j))
    out.discard((x, y))
    return out


this_turn = ferry.copy()
previous_turn = None
while this_turn != previous_turn:
    previous_turn = this_turn.copy()
    for i, row in enumerate(previous_turn):
        this_turn[i] = ""
        for j, space in enumerate(row):
            if space == ".":
                this_turn[i] += "."
                continue
            ns = [previous_turn[x][y] for x, y in neighbours(i, j)]
            if space == "#":
                if ns.count("#") >= 4:
                    this_turn[i] += "L"
                else:
                    this_turn[i] += space
            elif space == "L":
                if ns.count("#") == 0:
                    this_turn[i] += "#"
                else:
                    this_turn[i] += space

print(f"{''.join(this_turn).count('#')} seats filled")  # 2406

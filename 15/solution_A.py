import collections

puzzle_input = [0, 1, 4, 13, 15, 12, 16]

occurences = collections.defaultdict(list)
occurences.update({x: [i + 1] for i, x in enumerate(puzzle_input)})
last = 6
for i in range(len(puzzle_input) + 1, 2020 + 1):
    if len(occurences[last]) >= 2:
        a, b = occurences[last][-2:]
        x = b - a
    else:
        x = 0
    occurences[x].append(i)
    last = x

print(f"The 2020th number spoken in {x}")  # 1665

with open("adapters.txt") as file:
    adapters = sorted([int(i) for i in file])

possible_solutions = 1
previous = 0
last = max(adapters) + 3
for node, next_node in zip(adapters, [*adapters[1:], last]):
    if node - previous == 1:
        if next_node - previous == 3:  # current node can be skipped
            possible_solutions += 1
        if next_node - previous < 3:
            possible_solutions += 2
    previous = node

print(possible_solutions)  # 2027 too low

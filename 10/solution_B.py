with open("adapters.txt") as file:
    adapters = sorted([int(i) for i in file])

skippable = 1
previous = 0
last = max(adapters) + 3
for node, next_node in zip(adapters, [*adapters[1:], last]):
    if node - previous == 1:
        print(node, next_node)
        if next_node - previous <= 3:  # current node can be skipped
            skippable += 1
    previous = node

print((skippable ** 2) + 2)  # 2027 too low

# 0 to first always 3
# last to device always 3

# for 4 skippables
# all in

# 1, 2, 3, 4

# 1 + 2, 1 + 3, 1 + 4
# 2 + 3, 2 + 4
# 3 + 4
# ^ (4 - 1) ** 2 + (4 - 1)

# 1 + 2 + 3, 1 + 2 + 4, 1 + 3 + 4
# 2 + 3 + 4

...

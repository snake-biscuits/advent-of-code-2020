with open("adapters.txt") as file:
    adapters = sorted([int(i) for i in file])

previous = 0
differences = {1: 0, 2: 0, 3: 1}  # +1 for jump to final device
while len(adapters) > 0:
    differences[adapters[0] - previous] += 1
    previous = adapters.pop(0)

print(f"Answer is: {differences[1] * differences[3]}")

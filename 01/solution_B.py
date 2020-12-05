with open("numbers.txt") as file:
    numbers = [int(n) for n in file.readlines()]

for i, x in enumerate(numbers):
    for j, y in enumerate(numbers[i + 1:]):
        for k, z in enumerate(numbers[j + 1:]):
            if x + y + z == 2020:
                print(f"{x} * {y} * {z} = {x * y * z}")  # 171933104
                break

with open("numbers.txt") as file:
    numbers = [int(n) for n in file.readlines()]

for i, x in enumerate(numbers):
    for j, y in enumerate(numbers[i + 1:]):
        if x + y == 2020:
            print(f"{x} * {y} = {x * y}")  # 988771
            break

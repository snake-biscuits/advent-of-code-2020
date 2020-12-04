with open("numbers.txt") as file:
    numbers = [int(n) for n in file.readlines()]


if __name__ == "__main__":
    for i, x in enumerate(numbers):
        for j in range(i + 1, len(numbers)):
            y = numbers[j]
            for k in range(j + 1, len(numbers)):
                z = numbers[k]
                if x + y + z == 2020:
                    print(f"{x} * {y} * {z} = {x * y * z}")
                    break

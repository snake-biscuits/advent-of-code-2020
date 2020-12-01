with open("numbers.txt") as file:
    numbers = [int(n) for n in file.readlines()]


def main():
    for i, x in enumerate(numbers):
        for j in range(i + 1, len(numbers)):
            y = numbers[j]
            if x + y == 2020:
                print(f"{x} * {y} = {x * y}")
                return


main()

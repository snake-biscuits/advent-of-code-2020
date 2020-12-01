import get_numbers


if __name__ == "__main__":
    for i, x in enumerate(get_numbers.numbers):
        for j in range(i + 1, len(get_numbers.numbers)):
            y = get_numbers.numbers[j]
            if x + y == 2020:
                print(f"{x} * {y} = {x * y}")
                break

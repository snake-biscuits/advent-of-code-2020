from itertools import combinations


with open("encrypted_data.txt") as file:
    numbers = [int(i) for i in file]

for i, number in enumerate(numbers[25:]):
    i = i + 25
    if number not in (a + b for a, b in combinations(numbers[i-25:i], 2)):
        print(f"#{i:04}: {number} does not meet requirements")  # 32321523
        break

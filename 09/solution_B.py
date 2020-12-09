with open("encrypted_data.txt") as file:
    numbers = [int(i) for i in file]

for i, number in enumerate(numbers):
    seq = [number]
    j = i + 1
    while sum(seq) < 32321523:
        seq.append(numbers[j])
        j += 1
    if sum(seq) == 32321523:
        print(f"{min(seq) + max(seq) = }")  # 4794981
        break

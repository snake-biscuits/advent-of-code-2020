with open("passwords.txt") as file:
    inputs = [p.rstrip("\n") for p in file.readlines()]

valid_passwords = list()
for line in inputs:
    policy, password = line.split(": ")
    min_max, char = policy.split(" ")
    min_char, max_char = [int(x) for x in min_max.split("-")]
    if min_char <= password.count(char) <= max_char:
        valid_passwords.append(password)

print(f"Found {len(valid_passwords)} valid passwords")  # 393

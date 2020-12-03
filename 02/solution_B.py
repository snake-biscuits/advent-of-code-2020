with open("passwords.txt") as file:
    inputs = [p.rstrip("\n") for p in file.readlines()]


if __name__ == "__main__":
    valid_passwords = list()
  
    for line in inputs:
        policy, password = line.split(": ")
        indices, char = policy.split(" ")
        index_a, index_b = [int(i) - 1 for i in indices.split("-")]
        if (password[index_a] == char) ^ (password[index_b] == char):  # xor
            valid_passwords.append(password)  # 836 too high
    
    print(f"Found {len(valid_passwords)} valid passwords")

with open("passwords.txt") as file:
    inputs = [p.rstrip("\n") for p in file.readlines()]


if __name__ == "__main__":
    invalid_passwords = list()
  
    for line in inputs:
        policy, password = line.split(": ")
        min_max, char = policy.split(" ")
        min_char, max_char = [int(x) for x in min_max.split("-")]
        if not min_char <= password.count(char) <= max_char:
            print(f"{min_char} <= {password.count(char)} <= {max_char}")
        if min_char <= password.count(char) <= max_char:
            invalid_passwords.append(password)            
    
    print(f"Found {len(invalid_passwords)} invalid passwords")

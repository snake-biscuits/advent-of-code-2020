passports = list()
with open("passports.txt") as file:
    current_passport = dict()
    for line in file:
        if line == "\n":
            passports.append(current_passport)
            current_passport = dict()
        else:
            key_value_pairs = line.rstrip("\n").split()
            for pair in key_value_pairs:
                key, value = pair.split(":")
                current_passport[key] = value
    if len(current_passport) > 0:  # ensure the last entry is added
        passports.append(current_passport)


required_fields = {"byr",  # birth year
                   "iyr",  # issue year
                   "eyr",  # expiration year
                   "hgt",  # height
                   "hcl",  # hair colour
                   "ecl",  # eye colour
                   "pid"}  # passport ID
# ^ ignoring "cid" (country ID)

valid_count = 0
for passport in passports:
    if set(passport.keys()).intersection(required_fields) == required_fields:
        valid_count += 1

print(f"Found {valid_count} valid passports")  # 256

import re


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


def is_between(value, at_least=0, at_most=1):
    return at_least <= int(value) <= at_most


def check_height(string):
    check_for = {"cm": lambda v: is_between(v, 150, 193),
                 "in": lambda v: is_between(v, 59, 76)}
    value, units = string[:-2], string[-2:]
    if units not in ("cm", "in"):
        return False
    else:
        return check_for[units](value)


checks = {"byr": lambda v: is_between(v, 1920, 2002),
          "iyr": lambda v: is_between(v, 2010, 2020),
          "eyr": lambda v: is_between(v, 2020, 2030),
          "hgt": lambda v: check_height(v),
          "hcl": lambda v: bool(re.match(r"^#[0-9a-f]{6}$", v)),
          "ecl": lambda v: v in ("amb", "blu", "brn", "gry", "grn", "hzl", "oth"),
          "pid": lambda v: bool(re.match(r"^[0-9]{9}$", v))}

valid_count = 0
for passport in passports:
    if set(passport.keys()).intersection(required_fields) == required_fields:
        for key in required_fields:
            value = passport[key]
            if not checks[key](value):
                break
        else:
            valid_count += 1

print(f"Found {valid_count} valid passports")  # 198

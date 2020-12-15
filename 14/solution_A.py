import re


with open("program.txt") as file:
    instructions = [line for line in file]


def apply_mask(value, bitmask):
    bs = [b if o == "X" else o for b, o in zip(f"{value:038b}"[2:], bitmask)]
    return int(f"0b{''.join(bs)}", 2)


bitmask = ""
mem_string = r"mem\[(?P<address>[0-9]+)\] = (?P<value>[0-9]+)"
memory = dict()
for instruction in instructions:
    if instruction.startswith("mask = "):
        bitmask = instruction.split(" = ")[1]
    else:
        address, value = re.match(mem_string, instruction).groups()
        memory[address] = apply_mask(int(value), bitmask)

print(f"Answer is {sum(memory.values()) = }")  # 11327140210986

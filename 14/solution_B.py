import re


with open("program.txt") as file:
    instructions = [line for line in file]



def floating(x, bitmask):
    # print("=" * 40)
    base = [b if o == "X" else o for b, o in zip(f"{x:#038b}"[2:], bitmask)]
    # print(f"0b{''.join(base)}")
    # print(f"--{bitmask}")
    # print("-" * 40)
    for i in range(2 ** bitmask.count("X")):
        floating_address = []
        j = 0
        override = bin(i)[2:]
        override = ("0" * (bitmask.count("X") - len(override))) + override
        # print(override)
        for b, o in zip(base, bitmask):
            if o == "X":
                floating_address.append(override[j])
                j += 1
            else:
                floating_address.append(b)
            
        # print(f"0b{''.join(floating_address)}")
        yield int(f"0b{''.join(floating_address)}", 2)


bitmask = ""
memory = dict()
mem_string = r"mem\[(?P<address>[0-9]+)\] = (?P<value>[0-9]+)"
for instruction in instructions:
    if instruction.startswith("mask = "):
        bitmask = instruction.split(" = ")[1]
    else:
        address, value = re.match(mem_string, instruction).groups()
        for address in floating(int(address), bitmask):
            memory[address] = int(value)

print(f"Answer is {sum(memory.values()) = }")  # 780822017400 too low

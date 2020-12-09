with open("instructions.txt") as file:
    instructions = [(f, int(a)) for f, a in (i.split() for i in file)]

accumulator = 0
program_counter = 0
executed_lines = set()
while program_counter not in executed_lines:
    function, value = instructions[program_counter]
    print(f"{program_counter:04}:    {function} {value}")
    executed_lines.add(program_counter)
    if function == "acc":
        accumulator += value
        program_counter += 1
    elif function == "jmp":
        print("-" * 20)
        program_counter += value
    elif function == "nop":
        program_counter += 1
print(f"{program_counter:04}:    {function} {value}")

print(f"accumulator value is {accumulator}")  # 1797

with open("instructions.txt") as file:
    instructions = [(f, int(a)) for f, a in (i.split() for i in file)]

program_counter = 0
flipped_instructions = set()
while program_counter < len(instructions) - 1:
    accumulator = 0
    program_counter = 0
    executed_lines = set()
    flipped = False  # flip once per run
    while program_counter not in executed_lines:
        function, argument = instructions[program_counter]
        executed_lines.add(program_counter)
        if function == "acc":
            accumulator += argument
            program_counter += 1
        elif function == "jmp":
            if not flipped:
                if program_counter not in flipped_instructions:
                    print("nop", argument)
                    flipped = True
                    flipped_instructions.add(program_counter)
##                    print(f"flipped {program_counter}")
                    pass  # treat as nop
            program_counter += argument
        elif function == "nop":
            if not flipped:
                if program_counter not in flipped_instructions:
                    if argument == 0:  # skip nop 0
                        flipped_instructions.add(program_counter)
                    else:
                        print("jmp", argument)
                        flipped = True
                        flipped_instructions.add(program_counter)
##                        print(f"flipped {program_counter}")
                        program_counter += argument - 1  # treat as jmp
            program_counter += 1
    print(program_counter)
##    print(flipped_instructions)
    print("-" * 30)

print(f"accumulator value is {accumulator}")

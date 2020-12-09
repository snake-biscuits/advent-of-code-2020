with open("instructions.txt") as file:
    instructions = [(f, int(a)) for f, a in (i.split() for i in file)]


def run_asm(code):
    acc = 0
    executed = set()
    pc = 0
    while pc not in executed:
        func, arg = code[pc]
        if func == "acc":
            acc += arg
            pc += 1
        elif func == "jmp":
            yield pc
            pc += arg
        elif func == "nop":
            yield pc
            pc += 1

        if pc == len(code):
            print(f"Successfully Executed. {acc = }")
            return
    return  # run failed


flipped_instructions = set()
for flippable in run_asm(instructions):  # the yielded
    modded_code = instructions
    flipped = (??? if f else ???, a for f, a in modded_code[flippable])
    modded_code[flippable] = flipped
    run = list(run_asm(modded_code))

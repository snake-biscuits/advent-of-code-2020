with open("instructions.txt") as file:
    instructions = [(f, int(a)) for f, a in (i.split() for i in file)]


def run_asm(code):
    acc = 0
    executed = set()
    pc = 0
    while pc not in executed:
        executed.add(pc)
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


for index_to_flip in run_asm(instructions):  # the yielded
    modded_code = instructions.copy()
    func, arg = instructions[index_to_flip]
    if (func, arg) == ("nop", 0):
        continue  # don't flip: nop 0
    func = "jmp" if func == "nop" else "nop"
    modded_code[index_to_flip] = (func, arg)
    run = list(run_asm(modded_code))

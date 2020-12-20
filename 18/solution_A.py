import re


with open("homework.txt") as file:
    buffer = ""
    ops = {"+": lambda a, b: a + b,
           "*": lambda a, b: a * b}
    operation = ops["+"]
    results = [0]
    depth = 0
    question = file.readline().rstrip("\n")
    for char in question:
        if char == " ":
            if re.match(r"[0-9]+", buffer):
                results_depth = [] last_op(buffer, result)
                buffer = ""
            else:
                operation = ops[buffer]
                buffer = ""
        elif char == "("
        buffer += char

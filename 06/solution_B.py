all_group_answers = list()
current_group = set()
previous_line = ""
with open("answers.txt") as file:
    for line in file:
        line = line.rstrip("\n")
        if line == "":  # end of group's response
            all_group_answers.append(current_group)
            current_group = set()
        else:  # group answers
            if previous_line == "":  # first member's answers
                current_group = set(line)
            else:  # another member's answers
                current_group = current_group.intersection(set(line))
        previous_line = line
    if len(current_group) > 0:  # don't forget the last group
        all_group_answers.append(current_group)

print(f"The sum of all unanimous 'yes' answers is {sum([len(g) for g in all_group_answers])}")  # 3473

all_group_answers = list()
current_group = set()
with open("answers.txt") as file:
    for line in file:
        line = line.rstrip("\n")
        if line == "":  # end of group's response
            all_group_answers.append(current_group)
            current_group = set()
        else:  # a member's answers
            current_group.update(set(line))
    if len(current_group) > 0:  # don't forget the last group
        all_group_answers.append(current_group)

print(f"The sum of all 'yes' answers by group is {sum([len(g) for g in all_group_answers])}")  # 6911

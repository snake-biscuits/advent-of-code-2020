import collections
import re


bag_pattern = r"(?P<quantity>[0-9]+) (?P<colour>[a-z\ ]+)"
nodes = collections.defaultdict(dict)
# ^ bag_colour: {child: quantity}
with open("rules.txt") as file:
    for rule in file:
        rule = rule.split(" bag")
        parent = rule[0]
        children = rule[1:-1]
        if "no other" in children[0]:
            continue  # this bag is empty
        for child in rule[1:-1]:
            bag = re.search(bag_pattern, child).groupdict()
            nodes[parent][bag["colour"]] = int(bag["quantity"])


def contents_of(bag_colour):
    total = 0
    for child, quantity in nodes[bag_colour].items():
        total += quantity * contents_of(child)
    print(bag_colour, "contains:", total, "bags")
    return total if total != 0 else 1


print(f"shiny gold bag can contain a total of {contents_of('shiny gold')} bags")
# 145043 too low
# 172247 too high

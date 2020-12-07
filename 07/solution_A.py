import collections
import itertools
import re


bag_pattern = r"(?P<quantity>[0-9]+) (?P<colour>[a-z\ ]+)"
nodes = collections.defaultdict(list)
# ^ bag_type: [*parents]
with open("rules.txt") as file:
    for rule in file:
        rule = rule.split(" bag")
        parent = rule[0]
        children = rule[1:-1]
        if "no other" in children[0]:
            continue  # this bag is empty
        for child in rule[1:-1]:
            bag = re.search(bag_pattern, child).groupdict()
            nodes[bag["colour"]].append(parent)

ancestors = set()
tier = nodes["shiny gold"]
generations = 0
while len(tier) > 0:
    ancestors.update(tier)
    tier = set(itertools.chain(*[nodes[b] for b in tier]))
    generations += 1

print(f"shiny gold bag has {len(ancestors)} total ancestors across {generations} generations")

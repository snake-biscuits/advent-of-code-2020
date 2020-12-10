import collections
import math


with open("adapters.txt") as file:
    adapters = sorted([int(i) for i in file])

first, last = 0, max(adapters) + 3
for node in adapters:
    ????????????

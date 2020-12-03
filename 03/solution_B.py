with open("track.txt") as file:
    track = [line.rstrip("\n") for line in file]

def check_slope(track=track, right=3, down=1):
    track_width = len(track[0])  # track tiles to the right
    trees_hit, x = 0, 0
    for row in track[down::down]:
        x = (x + right) % track_width
        if row[x] == "#":
            trees_hit += 1
    return trees_hit

slope_1 = {"right": 1, "down": 1}
slope_2 = {"right": 3, "down": 1}
slope_3 = {"right": 5, "down": 1}
slope_4 = {"right": 7, "down": 1}
slope_5 = {"right": 1, "down": 2}
all_slopes = (slope_1, slope_2, slope_3, slope_4, slope_5)

runs = [check_slope(**slope) for slope in all_slopes]

slope_strings = [", ".join([f"{k} {v}" for k, v in d.items()]) for d in all_slopes]
for count, slope in zip(runs, slope_strings):
    print(f"Hit {count} trees along {slope}")

import math
print(f"Product of all runs is: {math.prod(runs)}")

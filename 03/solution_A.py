with open("track.txt") as file:
    track = [line.rstrip("\n") for line in file]


track_width = len(track[0])  # track tiles to the right
trees, x = 0, 0
for row in track[1:]:
    x = (x + 3) % track_width  # right 3, down 1
    if row[x] == "#":
        trees += 1

print(f"Hit {trees} trees")

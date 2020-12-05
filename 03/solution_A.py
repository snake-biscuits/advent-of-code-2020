with open("track.txt") as file:
    track = [line.rstrip("\n") for line in file]

track_width = len(track[0])
trees, x = 0, 0
for row in track[1:]:
    x = (x + 3) % track_width
    if row[x] == "#":
        trees += 1

print(f"Hit {trees} trees")  # 270

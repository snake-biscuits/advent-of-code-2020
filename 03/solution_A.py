with open("track.txt") as file:
    track = [line.rstrip("\n") for line in file]


track_width = len(track[0])  # track tiles to the right
trees = 0
x = 0
# print(track[0] * 3)
for row in track[1:]:
    true_x += 3  # right 3, down 1
    x = (x + 3) % track_width
    if row[x] == "#":
        trees += 1
        # print(row[:x], "X", row[x + 1:], sep="")  # debug
    # else:
    #     print(row[:true_x], "O", row[x + 1:], sep="")

print(f"Hit {trees} trees")

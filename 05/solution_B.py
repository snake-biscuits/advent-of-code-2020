with open("boarding_passes.txt") as file:
    all_seats = [int(f"0b{b.translate(dict(zip(map(ord, 'FBLR'), '0101')))}", 2) for b in file]
    print(f"My Seat ID is {set(range(min(all_seats), max(all_seats))).difference(set(all_seats))}")  # 717

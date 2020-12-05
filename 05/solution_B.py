with open("boarding_passes.txt") as file:
    all_seats = [int(f"0b{b.replace('F', '0').replace('B', '1').replace('L', '0').replace('R', '1')}", 2) for b in file]
    print(f"My Seat ID is {set(range(min(all_seats), max(all_seats))).difference(set(all_seats))}")

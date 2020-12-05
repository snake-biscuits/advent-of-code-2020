with open("boarding_passes.txt") as file:
    all_seats = [int(f"0b{b.replace('F', '0').replace('B', '1').replace('L', '0').replace('R', '1')}", 2) for b in file]
    start, end = min(all_seats), max(all_seats)

    my_seat = list(set(range(start, end)).difference(set(all_seats)))[0]

    print(f"My Seat ID is {my_seat} (Row {my_seat // 8}, {my_seat % 8})")

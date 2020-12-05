with open("boarding_passes.txt") as file:
    print(max([int(f"0b{b.replace('F', '0').replace('B', '1').replace('L', '0').replace('R', '1')}", 2) for b in file]))

with open("boarding_passes.txt") as file:
    print(max([int(f"0b{b.translate(dict(zip(map(ord, 'FBLR'), '0101')))}", 2) for b in file]))  # 913

with open("buses.txt") as file:
    file.readline()  # skip line 1
    bus_ids = [int(b) if b != "x" else None for b in file.read().split(",")]


delay = {b: i for i, b in enumerate(bus_ids) if b is not None}
# each bus leaves at t + delay[bus]

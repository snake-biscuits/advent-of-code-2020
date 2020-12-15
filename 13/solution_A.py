import collections


with open("buses.txt") as file:
    earliest, bus_ids = [line.rstrip("\n") for line in file]

earliest = int(earliest)
bus_ids = [int(b) for b in bus_ids.split(",") if b != "x"]

wait = collections.defaultdict(int)
for bus_id in bus_ids:
    length = bus_id - earliest % bus_id
    wait[length] = bus_id

shortest = min(wait)

print(f"ID of earliest bus: {wait[shortest]}, wait time: {shortest}")
print(f"Answer: {wait[shortest] * shortest}")  # 222

with open("ticket_notes.txt") as file:
    rules, my_ticket, nearby_tickets = file.read().split("\n\n")
    rules = rules.split("\n")
    my_ticket = [*map(int, my_ticket.split("\n")[1].split(","))]
    nearby_tickets = [[*map(int, t.split(","))] for t in nearby_tickets.split("\n")[1:]]

field_ranges = []
fields = []
for rule in rules:
    field, ranges = rule.split(": ")
    ranges = ranges.split(" or ")
    ranges = [tuple(map(int, r.split("-"))) for r in ranges]
    field_ranges.extend(ranges)
    fields.append(field)

invalid_tickets = []
for ticket in nearby_tickets:
    for i, x in enumerate(ticket):
        if not any([mi <= x <= ma for mi, ma in field_ranges]):
            invalid_tickets.append(ticket)
            break  # next ticket

tickets = set(nearby_tickets).difference(set(invalid_tickets))

# Answer: my_ticket 6 departure_* fields' product

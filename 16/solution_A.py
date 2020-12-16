with open("ticket_notes.txt") as file:
    rules, my_ticket, nearby_tickets = file.read().split("\n\n")
    rules = rules.split("\n")
    my_ticket = [*map(int, my_ticket.split("\n")[1].split(","))]
    nearby_tickets = [[*map(int, t.split(","))] for t in nearby_tickets.split("\n")[1:]]

field_ranges = []
for rule in rules:
    field, ranges = rule.split(": ")
    ranges = ranges.split(" or ")
    ranges = [tuple(map(int, r.split("-"))) for r in ranges]
    field_ranges.extend(ranges)

ticket_scanning_error_rate = 0
for ticket in nearby_tickets:
    for x in ticket:
        if not any([mi <= x <= ma for mi, ma in field_ranges]):
            ticket_scanning_error_rate += x

print(f"Ticket Scanning Error Rate: {ticket_scanning_error_rate}")

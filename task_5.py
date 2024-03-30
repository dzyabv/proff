import csv

with open('r/space.txt', 'r', encoding='utf-8') as file:
    ships = list(csv.DictReader(file, delimiter='*'))

hash = {}
for ship in ships:
    if ship[1] not in hash:
        hash[ship[1]] = ship[0]
    else:
        hash[ship[1]] += ship[0]

print(hash)
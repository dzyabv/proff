import csv

with open('space.txt', encoding='utf-8') as file:
    reader = csv.reader(file, delimiter='*')
    ships = list(reader)[1:]
    new_place = {}
    for ship_name, planet, coord_place, direction in ships:
        if '0 0' in coord_place:
            direction = direction.split()
            print(coord_place, direction)
            if int(ship_name[5]) > 5:
                
                
                coord_place_x = str(int(ship_name[5]) + int(direction[0]))
            else:
                coord_place_x = str((int(ship_name[5]) + int(direction[0])) * (-4) + len(planet))
            if int(ship_name[6]) > 3:
                coord_place_y = str(int(ship_name[6]) + len(planet) + int(direction[1]))
            else:
                coord_place_y = str((int(ship_name[5]) + int(direction[1])) * (int(ship_name[6])))
            coord_place = coord_place_x + ' ' + coord_place_y
            new_place[ship_name] = coord_place

for ship in ships:
    if '0 0' in ship[-2]:
        ship[-2] = new_place[ship_name]
    if ship[0][3] == 'V':
        d = ship[-2].split()
        print(f'{ship[0]} - ({d[0]}, {d[1]})')



with open('space_new.txt', 'w', encoding='utf-8') as file:
    writer = csv.writer(file, delimiter='*')
    writer.writerow(['ShipName', 'planet', 'coord_place', 'direction'])
    for ship in ships:
        #print(ship)
        writer.writerow(ship)

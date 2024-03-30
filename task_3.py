
import csv

with open('space.txt', 'r', encoding='utf-8') as file:
    ships = list(csv.DictReader(file, delimiter='*'))

ship_num = input()

while ship_num.lower() != 'stop' and ship_num != '':
    ship_num = input()
    for ship in ships:
        if ship_num == ship['ShipName']:
            print(f'Корабль {ship["ShipName"]} был отправлен с планеты: {ship["planet"]} и его направление движения было: {ship["direction"]}')
            break
    else:
        print('error.. er.. ror..')
        
        
    
ship_num = input()

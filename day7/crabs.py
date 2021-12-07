with open('./day7/input.txt') as f:
    crab_input = f.read().splitlines()
    
crab_list = list(map(int,crab_input[0].split(',')))

lowest_fuel = 100000000

for i in range(min(crab_list), max(crab_list)):
    total_fuel = 0
    move_loctation = i
    for crab in crab_list:
        total_movement = sum(range(0, abs(move_loctation - crab) + 1))
        total_fuel += total_movement
    if total_fuel < lowest_fuel:
        lowest_fuel = total_fuel

print(lowest_fuel)

with open('input-part1.txt') as f:
    sonar_input = list(map(int, f.read().splitlines())) 

increase_count = 0
last_depth = None

for depth in sonar_input:
    if (last_depth):
        if(depth > last_depth):
            increase_count += 1
    last_depth = depth

print(increase_count)
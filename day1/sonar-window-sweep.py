with open('input-part1.txt') as f:
    sonar_input = f.read().splitlines() 

sonar_input = list(map(int, sonar_input))
window_size = 3
increase_count = 0
last_depth = None

for i in range(len(sonar_input) - window_size + 1):
    depth = sum(sonar_input[i: i + window_size])
    if (last_depth):
        if(depth > last_depth):
            increase_count += 1
    last_depth = depth

print(increase_count)

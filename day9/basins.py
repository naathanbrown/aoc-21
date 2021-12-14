import math
with open('./day9/input.txt') as f:
    puzzle_input = f.read().splitlines()

heightmap = []
for input in puzzle_input:
    line_len = len(input)
    puzzle_line = []
    for number in input:
        puzzle_line.append(int(number))
    heightmap.append(puzzle_line)


risk = 0 
low_points = []  
for idx, line in enumerate(heightmap):
    for idy, number in enumerate(line):
        if idx == 0:
            #Top row
            if idy == 0:
                #Row below and number to right
                if number < heightmap[idx + 1][idy] and number < heightmap[idx][idy + 1]:
                    risk += 1 + number
                    low_points.append((idx, idy))
            elif idy == len(line) - 1:
                #Row below and number to left
                if number < heightmap[idx + 1][idy] and number < heightmap[idx][idy - 1]:
                    risk += 1 + number
                    low_points.append((idx, idy))
            else:
                #Row below, number left and right
                if number < heightmap[idx + 1][idy] and number < heightmap[idx][idy + 1] and number < heightmap[idx][idy - 1]:
                    risk += 1 + number
                    low_points.append((idx, idy))
        elif idx == len(heightmap) - 1:
            if idy == 0:
                #Row above and number to right
                if number < heightmap[idx - 1][idy] and number < heightmap[idx][idy + 1]:
                    risk += 1 + number
                    low_points.append((idx, idy))
            elif idy == len(line) - 1:
                #Row above and number to the left
                if number < heightmap[idx - 1][idy] and number < heightmap[idx][idy - 1]:
                    risk += 1 + number
                    low_points.append((idx, idy))
            else:
                #Row above, number left and right
                if number < heightmap[idx - 1][idy] and number < heightmap[idx][idy + 1] and number < heightmap[idx][idy - 1]:
                    risk += 1 + number
                    low_points.append((idx, idy))
        else:
            if idy == 0:
                #Row below and above, but just right
                if number < heightmap[idx + 1][idy] and number < heightmap[idx - 1][idy] and number < heightmap[idx][idy + 1]:
                    risk += 1 + number
                    low_points.append((idx, idy))
            elif idy == len(line) - 1:
                #Row above and below, but just left
                if number < heightmap[idx + 1][idy] and number < heightmap[idx - 1][idy] and number < heightmap[idx][idy - 1]:
                    risk += 1 + number
                    low_points.append((idx, idy))
            else:
                #check all positions
                if number < heightmap[idx + 1][idy] and number < heightmap[idx - 1][idy] and number < heightmap[idx][idy + 1] and number < heightmap[idx][idy - 1]:
                    risk += 1 + number
                    low_points.append((idx, idy))

#Rebuild and pad the board
heightmap = []
for input in puzzle_input:
    line_len = len(input)
    puzzle_line = []
    for number in input:
        puzzle_line.append(int(number))
    heightmap.append([9] + puzzle_line + [9])

heightmap = [[9] * (line_len + 2)] + heightmap
heightmap.append([9] * (line_len + 2))

#Update the low points
low_points_new = []
for low_point in low_points:
    low_points_new.append((low_point[0] + 1,low_point[1] + 1))

low_points = low_points_new

def check_low_points(low_points, basin):
    new_low_points = []
    for low_point in low_points:
        if heightmap[low_point[0]][low_point[1] + 1] != 9 and (low_point[0], low_point[1] + 1) not in basin:
            new_low_points.append((low_point[0], low_point[1] + 1))
            basin.add((low_point[0], low_point[1] + 1))

        if heightmap[low_point[0]][low_point[1] - 1] != 9 and (low_point[0], low_point[1] - 1) not in basin:
            new_low_points.append((low_point[0], low_point[1] - 1))
            basin.add((low_point[0], low_point[1] - 1))

        if heightmap[low_point[0] + 1][low_point[1]] != 9 and (low_point[0] + 1, low_point[1]) not in basin:
            new_low_points.append((low_point[0] + 1, low_point[1]))
            basin.add((low_point[0] + 1, low_point[1]))

        if heightmap[low_point[0] - 1][low_point[1]] != 9 and (low_point[0] - 1, low_point[1]) not in basin:
            new_low_points.append((low_point[0] - 1, low_point[1]))
            basin.add((low_point[0] - 1, low_point[1]))
    
    return new_low_points

list_of_basins = []
for low_point in low_points:
    basin = set()
    basin.add(low_point)
    res = check_low_points([low_point], basin)
    while res != []:
        res = check_low_points(res, basin)
    list_of_basins.append(len(basin))

total = math.prod(sorted(list_of_basins, reverse=True)[:3])
print(total)

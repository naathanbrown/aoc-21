with open('./day9/input.txt') as f:
    puzzle_input = f.read().splitlines()

heightmap = []
for input in puzzle_input:
    puzzle_line = []
    for number in input:
        puzzle_line.append(int(number))
    heightmap.append(puzzle_line)

risk = 0   
for idx, line in enumerate(heightmap):
    for idy, number in enumerate(line):
        if idx == 0:
            #Top row
            if idy == 0:
                #Row below and number to right
                if number < heightmap[idx + 1][idy] and number < heightmap[idx][idy + 1]:
                    risk += 1 + number
            elif idy == len(line) - 1:
                #Row below and number to left
                if number < heightmap[idx + 1][idy] and number < heightmap[idx][idy - 1]:
                    risk += 1 + number
            else:
                #Row below, number left and right
                if number < heightmap[idx + 1][idy] and number < heightmap[idx][idy + 1] and number < heightmap[idx][idy - 1]:
                    risk += 1 + number
        elif idx == len(heightmap) - 1:
            if idy == 0:
                #Row above and number to right
                if number < heightmap[idx - 1][idy] and number < heightmap[idx][idy + 1]:
                    risk += 1 + number
            elif idy == len(line) - 1:
                #Row above and number to the left
                if number < heightmap[idx - 1][idy] and number < heightmap[idx][idy - 1]:
                    risk += 1 + number
            else:
                #Row above, number left and right
                if number < heightmap[idx - 1][idy] and number < heightmap[idx][idy + 1] and number < heightmap[idx][idy - 1]:
                    risk += 1 + number
        else:
            if idy == 0:
                #Row below and above, but just right
                if number < heightmap[idx + 1][idy] and number < heightmap[idx - 1][idy] and number < heightmap[idx][idy + 1]:
                    risk += 1 + number
            elif idy == len(line) - 1:
                #Row above and below, but just left
                if number < heightmap[idx + 1][idy] and number < heightmap[idx - 1][idy] and number < heightmap[idx][idy - 1]:
                    risk += 1 + number
            else:
                #check all positions
                if number < heightmap[idx + 1][idy] and number < heightmap[idx - 1][idy] and number < heightmap[idx][idy + 1] and number < heightmap[idx][idy - 1]:
                    risk += 1 + number
print(risk)
class CoOrdinate:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = int(x1)
        self.y1 = int(y1)
        self.x2 = int(x2)
        self.y2 = int(y2)
    def CheckNonDiagonal(self):
        if (self.x1 == self.x2):
            return True
        elif (self.y1 == self.y2):
            return True
        else:
            return False

class SeaMap:
    def __init__(self, co_ord_list):
        highest_x = 0
        highest_y = 0
        for co_ord in co_ord_list:
            if co_ord.x1 > co_ord.x2:
                if co_ord.x1 > highest_x:
                    highest_x = co_ord.x1
            else:
                if co_ord.x2 > highest_x:
                    highest_x = co_ord.x2
            
            if co_ord.y1 > co_ord.y2:
                if co_ord.y1 > highest_y:
                    highest_y = co_ord.y1
            else:
                if co_ord.y2 > highest_y:
                    highest_y = co_ord.y2
        self.map = []
        for y in range(0, highest_y + 1):
            y_row = []
            for x in range(0, highest_x + 1):
                y_row.append(0)
            self.map.append(y_row)
    
    def MarkCoOrd(self, co_ord, diagonal):
        if co_ord.CheckNonDiagonal():
            if co_ord.y1 == co_ord.y2:
                y_row = co_ord.y1
                if co_ord.x1 <= co_ord.x2:
                    for i in range(co_ord.x1, co_ord.x2 + 1, 1):
                        self.map[y_row][i] += 1
                    return self.map
                else:
                    for i in range(co_ord.x1, co_ord.x2 -1, -1):
                        self.map[y_row][i] += 1
                    return self.map

            if co_ord.x1 == co_ord.x2:
                x_position = co_ord.x1
                if co_ord.y1 <= co_ord.y2:
                    for i in range(co_ord.y1, co_ord.y2 + 1, 1):
                        self.map[i][x_position] += 1
                    return self.map
                else:
                    for i in range(co_ord.y1, co_ord.y2 -1, -1):
                        self.map[i][x_position] += 1
                    return self.map
        elif diagonal == True:
            #Deal with our diagonal lines
            y_list = []
            x_list = []
            if co_ord.y1 <= co_ord.y2: 
                for i in range(co_ord.y1, co_ord.y2 + 1, 1):
                    y_list.append(i)
            else:
                for i in range(co_ord.y1, co_ord.y2 - 1, -1):
                    y_list.append(i)
            if co_ord.x1 <= co_ord.x2:
                for i in range(co_ord.x1, co_ord.x2 + 1, 1):
                    x_list.append(i)
            else:
                for i in range(co_ord.x1, co_ord.x2 -1 , -1):
                    x_list.append(i)
            for i in range(0, len(x_list)):
                self.map[y_list[i]][x_list[i]] += 1

    def CountOverTwo(self):
        over_two = 0
        for i in range(0, len(self.map)):
            for j in range(0, len(self.map[i])):
                if self.map[i][j] >= 2:
                    over_two += 1
        return over_two
                
    def ToString(self):
        for y in range(0, len(self.map)):
            print("Row ", y, self.map[y])

with open('./day5/input.txt') as f:
    line_input = f.read().splitlines()

co_ord_list = []

for line in line_input:
    x, y = line.split('->')
    x1, y1 = x.strip().split(',')
    x2, y2 = y.strip().split(',')
    co_ord = CoOrdinate(x1, y1, x2, y2)
    co_ord_list.append(co_ord)

sea_map = SeaMap(co_ord_list)

for co_ord in co_ord_list:
    #Toggle T/F to add in diagonals
    sea_map.MarkCoOrd(co_ord, False)

print(sea_map.CountOverTwo())

with open('input.txt') as f:
    direction_input = f.read().splitlines()

x_pos = 0
y_pos = 0

for direction in direction_input:
    direction_type = direction.split(' ')[0]
    direction_movement = int(direction.split(' ')[1])

    if direction_type == 'forward':
        x_pos += direction_movement
    elif direction_type == 'down':
        y_pos += direction_movement
    else:
        y_pos -= direction_movement

position = x_pos * y_pos

print(position)

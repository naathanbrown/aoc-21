with open('input.txt') as f:
    binary_input = f.read().splitlines()

binary_counter =  {}

for binary in binary_input:
    for idx, bit in enumerate(binary):
        if idx in binary_counter:
            if bit == "1":
                binary_counter[idx] += 1
            else:
                binary_counter[idx] -= 1
        else:
            binary_counter[idx] = 0
gamma = ""  
ep = ""
for key, value in binary_counter.items():
    if value >= 0:
        gamma += ("1")
        ep += ("0")
    else:
        gamma += ("0")
        ep += ("1")

gamma = int(gamma, 2)
ep = int(ep, 2)

print(ep * gamma)
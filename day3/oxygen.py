with open('input.txt') as f:
    binary_input = f.read().splitlines()

binary_most = binary_input
binary_least = binary_input 

binary_len = len(binary_input[0])

for i in range(binary_len):

    if (len(binary_most) == 1):
        break

    counter = 0
    for binary in binary_most:
        if binary[i] == "1":
            counter += 1
        else:
            counter -= 1
    
    if counter >= 0:
        most_common = "1"
    else:
        most_common = "0"
    
    remove_list = []
    for binary in binary_most:
        if binary[i] != most_common:
            remove_list.append(binary)

    binary_most = [x for x in binary_most if x not in remove_list]

for i in range(binary_len):

    if (len(binary_least) == 1):
        break

    counter = 0
    for binary in binary_least:
        if binary[i] == "1":
            counter += 1
        else:
            counter -= 1
    
    if counter >= 0:
        least_common = "0"
    else:
        least_common = "1"

    remove_list = []
    for binary in binary_least:
        if binary[i] != least_common:
           remove_list.append(binary)

    binary_least = [x for x in binary_least if x not in remove_list]

print(int(binary_least[0], 2) * int(binary_most[0], 2))
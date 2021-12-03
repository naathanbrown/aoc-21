def calculate_bit_criterion(binary_list, criteria):

    binary_len = len(binary_input[0])

    for i in range(binary_len):

        if (len(binary_list) == 1):
            return binary_list[0]
    
        counter = 0
        for binary in binary_list:
            if binary[i] == "1":
                counter += 1
            else:
                counter -= 1

        if criteria == "most":
            if counter >= 0:
                common_value = "1"
            else:
                common_value = "0"
        elif criteria == "least":
            if counter >= 0:
                common_value = "0"
            else:
                common_value = "1"
        else:
            print("must be most or least")
            break

        remove_list = []
        for binary in binary_list:
            if binary[i] != common_value:
                remove_list.append(binary)

        binary_list = [x for x in binary_list if x not in remove_list]
    
    return binary_list[0]

with open('input.txt') as f:
    binary_input = f.read().splitlines()

oxygen = calculate_bit_criterion(binary_input, "most")
scrubber = calculate_bit_criterion(binary_input, "least")

print(int(oxygen, 2) * int(scrubber, 2))
with open('./day8/input.txt') as f:
    wire_input = f.read().splitlines()

count = 0

value_output_score = 0

code_dict = {0:"", 1:"", 2:"", 3:"", 4:"", 5:"", 6:"", 7:"", 8:"", 9:""}

for wire in wire_input:
    wire_output = wire.split('|')[1].split(' ')
    for output in wire_output:
        if len(output) in [2,3,4,7]:
            count += 1
            #Work out the easy ones 
            if len(output) == 2:
                code_dict[1] = output
            if len(output) == 3:
                code_dict[7] = output
            if len(output) == 4:
                code_dict[4] = output
            if len(output) == 7:
                code_dict[8] = output

    wire_coded = wire.split('|')[0].split(' ')
    for code in wire_coded:
        #Work out the easy ones 
        if len(code) == 2:
            code_dict[1] = code
        if len(code) == 3:
            code_dict[7] = code
        if len(code) == 4:
            code_dict[4] = code
        if len(code) == 7:
            code_dict[8] = code

    if code_dict[1] != '' and code_dict[7] != '' and code_dict[4] != '' and code_dict[8] != '':
        position_dict = {"a" :"", "b" :"", "c" :"", "d": "", "e" : "", "f": "", "g": ""}
        x1 = list(code_dict[1])[0]
        x2 = list(code_dict[1])[1]
        x = x1 + x2
        position_dict["a"] = code_dict[7].replace(x1, "").replace(x2, "")
        y1 = list(code_dict[4].replace(x1,"").replace(x2,""))[0]
        y2 = list(code_dict[4].replace(x1,"").replace(x2,""))[1]
        y = y1 + y2
        z1 = list(code_dict[8].replace(x1,"").replace(x2,"").replace(y1,"").replace(y2,"").replace(position_dict["a"], ""))[0]
        z2 = list(code_dict[8].replace(x1,"").replace(x2,"").replace(y1,"").replace(y2,"").replace(position_dict["a"], ""))[1]
        z = z1 + z2

        solved_bool = False
        for code in wire_coded:
            if y1 in code and y2 in code and position_dict["a"] in code and len(code) == 5:
                position_dict["g"] = code.replace(y1, "").replace(y2, "").replace(position_dict["a"], "").replace(x1, "").replace(x2,"")
                position_dict["f"] = code.replace(y1, "").replace(y2, "").replace(position_dict["a"], "").replace(position_dict["g"], "")
                position_dict["e"] = z.replace(position_dict["g"], "")
                position_dict["c"] = x.replace(position_dict["f"], "")
                solved_bool = True
                break
        for code in wire_coded:
            if x1 in code and x2 in code and position_dict["a"] in code and len(code) == 5 and solved_bool:
                position_dict["d"] = code.replace(x1, "").replace(x2, "").replace(position_dict["a"], "").replace(position_dict["g"], "")
                position_dict["b"] = y.replace(position_dict["d"], "")

        if '' not in position_dict.values():
            code_list = []
            code_list.append([position_dict["a"],position_dict["b"],position_dict["c"],position_dict["e"],position_dict["f"],position_dict["g"]])#0
            code_list.append([position_dict["c"],position_dict["f"]])#1
            code_list.append([position_dict["a"],position_dict["c"],position_dict["d"],position_dict["e"],position_dict["g"]])#2
            code_list.append([position_dict["a"],position_dict["c"],position_dict["d"],position_dict["f"],position_dict["g"]])#3
            code_list.append([position_dict["b"],position_dict["c"],position_dict["d"],position_dict["f"]])#4
            code_list.append([position_dict["a"],position_dict["b"],position_dict["d"],position_dict["f"],position_dict["g"]])#5
            code_list.append([position_dict["a"],position_dict["b"],position_dict["d"],position_dict["e"],position_dict["f"],position_dict["g"]])#6
            code_list.append([position_dict["a"],position_dict["c"],position_dict["f"]])#7
            code_list.append([position_dict["a"],position_dict["b"],position_dict["c"],position_dict["d"],position_dict["e"],position_dict["f"],position_dict["g"]])#8
            code_list.append([position_dict["a"],position_dict["b"],position_dict["c"],position_dict["d"],position_dict["f"],position_dict["g"]])#9
        else:
            print("error")
            print(position_dict)

        value_output = ""
        for output in wire_output:
            if output != '':
                for idx, code in enumerate(code_list):
                    if set(code) == set(output):
                        value_output += (str(idx))
        if len(value_output) == 4: 
            value_output_score += int(value_output)
        else:
            print("error", value_output)
            print(position_dict)


print(value_output_score)
print(count)
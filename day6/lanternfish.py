with open('./day6/input.txt') as f:
    fish_input = f.read().splitlines()

fish_list = list(map(int,fish_input[0].split(',')))

bucket = {-1:0, 0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0}

for fish in fish_list:
    bucket[fish] +=1

for i in range(0, 256):

    for j in range(0, 9):
        bucket[j - 1] = bucket[j]

    bucket[8] = bucket[-1]
    bucket[6] += bucket[-1]
    bucket[-1] = 0

print(sum(bucket.values()))
file = open('input.txt', 'r')
input = file.readlines()

horizontal = 0
depth = 0
aim = 0

for data in input:
    subData = data.split(' ')
    if subData[0] == "forward":
        horizontal += int(subData[1])
        depth += aim * int(subData[1])
    if subData[0] == "up":
        aim -= int(subData[1])
    if subData[0] == "down":
        aim += int(subData[1])

print(horizontal*depth)
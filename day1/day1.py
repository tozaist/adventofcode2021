file = open('input.txt', 'r')
input = file.readlines()

count = 0
i = 0
oldDepth = int(input[i]) + int(input[i + 1]) + int(input[i + 2])

i+=1
while i < len(input)-2:
    depth = int(input[i]) + int(input[i + 1]) + int(input[i + 2])
    if depth > oldDepth:
        count += 1
    oldDepth = depth
    i+=1
print(count)
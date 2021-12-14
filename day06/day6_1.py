file1 = open('input.txt', 'r')
line = file1.readline()

tmp = line.split(',')
numbers = []
for val in tmp:
    numbers.append(int(val))

for day in range(0, 80):
    oldSize = len(numbers)
    for i in range(0, oldSize):
        if numbers[i] == 0:
            numbers[i] = 6
            numbers.append(8)
        else:
            numbers[i] -= 1

print(len(numbers))
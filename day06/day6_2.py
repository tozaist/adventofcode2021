file1 = open('input.txt', 'r')
line = file1.readline()

tmp = line.split(',')
numbers = []
for val in tmp:
    numbers.append(int(val))

fishes = [0] * 9

for fish in numbers:
    fishes[fish] += 1
for day in range(256):
    tmp = fishes[0]
    for i in range(1, len(fishes)):
        fishes[i - 1] = fishes[i]
    fishes[6] += tmp
    fishes[8] = tmp

sum = 0
for fish in fishes:
    sum += fish

print(sum)
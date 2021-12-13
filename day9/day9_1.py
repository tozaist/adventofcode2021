file1 = open('input.txt', 'r')
lines = file1.readlines()

numbers = []
for i in range(len(lines)):
    numbers.append([])
    for j in range(len(lines[i])):
        if lines[i][j] != '\n':
            numbers[i].append(int(lines[i][j]))

output = 0
for i in range(len(numbers)):
    for j in range(len(numbers[i])):
        if i > 0:
            if numbers[i][j] >= numbers[i - 1][j]:
                continue
        if i < len(numbers) - 1:
            if numbers[i][j] >= numbers[i + 1][j]:
                continue
        if j > 0:
            if numbers[i][j] >= numbers[i][j - 1]:
                continue
        if j < len(numbers[i]) - 1:
            if numbers[i][j] >= numbers[i][j + 1]:
                continue
        output += 1 + numbers[i][j]
print(output)
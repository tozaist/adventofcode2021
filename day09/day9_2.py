def find_basin(a, b):
    
    size = 1
    visited[a][b] = True
    
    adjacents = []
    tmp = []
    if a > 0:
        tmp = [a - 1, b]
        if numbers[tmp[0]][tmp[1]] < 9 and not visited[tmp[0]][tmp[1]]:
            adjacents.append(tmp)
    if a < len(numbers) - 1:
        tmp = [a + 1, b]
        if numbers[tmp[0]][tmp[1]] < 9 and not visited[tmp[0]][tmp[1]]:
            adjacents.append(tmp)
    if b > 0:
        tmp = [a, b - 1]
        if numbers[tmp[0]][tmp[1]] < 9 and not visited[tmp[0]][tmp[1]]:
            adjacents.append(tmp)
    if b < len(numbers[a]) - 1:
        tmp = [a, b + 1]
        if numbers[tmp[0]][tmp[1]] < 9 and not visited[tmp[0]][tmp[1]]:
            adjacents.append(tmp)

    for adjacent in adjacents:
        if not visited[adjacent[0]][adjacent[1]]:
            size += find_basin(adjacent[0], adjacent[1])

    return size

file1 = open('input.txt', 'r')
lines = file1.readlines()

numbers = []
visited = []
for i in range(len(lines)):
    numbers.append([])
    visited.append([])
    for j in range(len(lines[i])):
        if lines[i][j] != '\n':
            numbers[i].append(int(lines[i][j]))
            visited[i].append(False)

basins = []
for i in range(len(numbers)):
    for j in range(len(numbers[i])):
        if numbers[i][j] < 9 and not visited[i][j]:
            basins.append(find_basin(i, j))
basins.sort()
print(basins[-1] * basins[-2] * basins[-3])
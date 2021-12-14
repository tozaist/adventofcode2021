def increase_energy(a, b):
    octopuses[a][b] += 1
    if octopuses[a][b] > 9:
        octopuses[a][b] = -99999
        flashes[a][b] = True
        adjacents = []
        if a > 0:
            tmp = [a - 1, b]
            adjacents.append(tmp)
            if b > 0:
                tmp = [a - 1, b - 1]
                adjacents.append(tmp)
            if b < len(octopuses[a])-1:
                tmp = [a - 1, b + 1]
                adjacents.append(tmp)
        if a < len(octopuses)-1:
            tmp = [a + 1, b]
            adjacents.append(tmp)
            if b > 0:
                tmp = [a + 1, b - 1]
                adjacents.append(tmp)
            if b < len(octopuses[a])-1:
                tmp = [a + 1, b + 1]
                adjacents.append(tmp)
        if b > 0:
            tmp = [a, b - 1]
            adjacents.append(tmp)
        if b < len(octopuses[a])-1:
            tmp = [a, b + 1]
            adjacents.append(tmp)
        for adjacent in adjacents:
            increase_energy(adjacent[0], adjacent[1])
        
file1 = open('input.txt', 'r')
lines = file1.readlines()

octopuses=[]
flashes=[]
for i in range(len(lines)):
    octopuses.append([])
    flashes.append([])
    for char in lines[i]:
        if char != '\n':
            octopuses[i].append(int(char))
            flashes[i].append(False)

step = 0
while True:
    step += 1
    for i in range(len(octopuses)):
        for j in range(len(octopuses[i])):
            increase_energy(i, j)


    condition = True
    for i in range(len(flashes)):
        for j in range(len(flashes)):
            if not flashes[i][j]:
                condition = False
            if flashes[i][j]:
                octopuses[i][j] = 0
                flashes[i][j] = False
    if condition:
        print(step)
        break

import numpy as np
file1 = open('input.txt', 'r')
lines = file1.readlines()
maxX = 0
maxY = 0
for line in lines:
    ab = line.split(' -> ')
    a = ab[0].split(',')
    b = ab[1].split(',')
    x1 = int(a[0])
    y1 = int(a[1])
    x2 = int(b[0])
    y2 = int(b[1])
    maxX = max(x1, x2, maxX)
    maxY = max(y1, y2, maxY)

coords = np.zeros((maxX + 1, maxY + 1))

for line in lines:
    ab = line.split(' -> ')
    a = ab[0].split(',')
    b = ab[1].split(',')
    x1 = int(a[0])
    y1 = int(a[1])
    x2 = int(b[0])
    y2 = int(b[1])
    if x1 == x2:
        for i in range(min(y1, y2), max(y1, y2) + 1):
            coords[x1][i] += 1
    elif y1 == y2:
        for i in range(min(x1, x2), max(x1, x2) + 1):
            coords[i][y1] += 1


count = 0
for i in range(0, len(coords)):
    for j in range(0, len(coords[i])):
        if coords[i][j] > 1:
            count += 1
print(count)
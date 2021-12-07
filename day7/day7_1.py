file1 = open('input.txt', 'r')
line = file1.readline().split(',')
crabs = []
for crab in line:
    crabs.append(int(crab))

costs = [0] * max(crabs)
for i in range(max(crabs)):
    for crab in crabs:
        costs[i] += abs(crab - i)

print(min(costs))
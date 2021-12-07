file1 = open('input.txt', 'r')
line = file1.readline().split(',')
crabs = []
for crab in line:
    crabs.append(int(crab))

costs = [0] * max(crabs)
for i in range(max(crabs)):
    for crab in crabs:                  
        n = abs(crab - i)               # n_{i+1} = n_i + 1
        costs[i] += (n + n ** 2) / 2    

print(min(costs))
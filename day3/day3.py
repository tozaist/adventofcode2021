file = open('input.txt', 'r')
input = file.readlines()

count = len(input)

occurances = [0] * (len(input[0]) - 1)
gamma = [0] * (len(input[0]) - 1)
epsilon = [0] * (len(input[0]) - 1)

for data in input:
    i=0
    while i < len(data):
        if data[i] == '1':
            occurances[i] += 1
        i+=1

i=0
while i < len(occurances):
    if occurances[i] > count/2:
        gamma[i] = 1
        epsilon[i] = 0
    else:
        gamma[i] = 0
        epsilon[i] = 1
    i+=1

i=0
iGamma=0
while i < len(gamma):
    iGamma+=int(gamma[len(gamma)-1 - i]) * pow(2, i)
    i+=1

i=0
iEpsilon =0
while i < len(epsilon):
    iEpsilon+=int(epsilon[len(epsilon)-1 - i]) * pow(2, i)
    i+=1

print(iGamma * iEpsilon)
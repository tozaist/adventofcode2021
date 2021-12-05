from typing import IO


file = open('input.txt', 'r')
input = file.readlines()

count = len(input)
values = input.copy()
leftValues = []
occurances = 0

for i in range(0, len(input[0])):
    if len(values) == 1:
        break
    occurances = 0
    count = len(values)
    for j in range(0, len(values)):
        if values[j][i] == '1':
            occurances += 1

    leftValues.clear()
    for data in values:
        if occurances >= count/2:
            if data[i] == '1':
                leftValues.append(data)
        else:
            if data[i] == '0':
                leftValues.append(data)
    values = leftValues.copy()

oxygenRate = leftValues[0]

values = input.copy()
occurances = 0
leftValues = []

for i in range(0, len(input[0])):
    if len(values) == 1:
        break
    occurances = 0
    count = len(values)
    for j in range(0, len(values)):
        if values[j][i] == '1':
            occurances += 1

    leftValues.clear()
    for data in values:
        if occurances < count/2:
            if data[i] == '1':
                leftValues.append(data)
        else:
            if data[i] == '0':
                leftValues.append(data)
    values = leftValues.copy()

co2Rate = leftValues[0]

oxygenRate = oxygenRate[:-1]
co2Rate = co2Rate[:-1]
print (oxygenRate, " ", co2Rate)
i=0
iOxygenRate=0
while i < len(oxygenRate):
    iOxygenRate+=int(oxygenRate[len(oxygenRate)-1 - i]) * pow(2, i)
    i+=1

i=0
iCo2Rate =0
while i < len(co2Rate):
    iCo2Rate+=int(co2Rate[len(co2Rate)-1 - i]) * pow(2, i)
    i+=1

print(iOxygenRate * iCo2Rate)
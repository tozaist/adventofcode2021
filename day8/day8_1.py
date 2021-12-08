file1 = open('input.txt', 'r')
lines = file1.readlines()

count = 0
for line in lines:
    data = line.split('|')
    numbers = data[1].split()
    for number in numbers:
        if len(number) == 2 or len(number) == 3 or len(number) == 4 or len(number) == 7:
            count += 1 
print(count)
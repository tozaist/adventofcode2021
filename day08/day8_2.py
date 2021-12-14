file1 = open('input.txt', 'r')
lines = file1.readlines()

sum = 0
for line in lines:
    data = line.split('|')
    numbers = data[0].split()
    i=0
    right = []
    bot_left = 0
    center = 0
    while True:
        if len(numbers[i]) == 2:
            right.append(numbers[i][0])
            right.append(numbers[i][1])

        i+=1
        if i == len(numbers):
            i=0

        if len(right) != 0:
            break
    i=0
    possible_centers = []
    while True:
        if len(numbers[i]) == 4:
            possible_centers = numbers[i]
            possible_centers = possible_centers.replace(right[0], '')
            possible_centers = possible_centers.replace(right[1], '')

        if len(numbers[i]) == 5 and len(possible_centers) != 0 and right[0] in numbers[i] and right[1] in numbers[i]:
            for char in numbers[i]:
                if char in possible_centers:
                    center = char
                    break

        i+=1
        if i == len(numbers):
            i=0

        if center != 0:
            break   

    i=0
    while True:
        if len(numbers[i]) == 6 and center in numbers[i] and right[0] in numbers[i] and right[1] in numbers[i]:
            tmp = "abcdefg"
            for char in numbers[i]:
                tmp = tmp.replace(char, '')
            bot_left = tmp[0]

        i+=1
        if i == len(numbers):
            i=0

        if bot_left != 0:
            break

    count = []
    numbers = data[1].split()
    for number in numbers:
        match len(number):
            case 2:
                count.append(1)
            case 3:
                count.append(7)
            case 4:
                count.append(4)
            case 5:
                if right[0] in number and right[1] in number:
                    count.append(3)
                else:
                    if bot_left in number:
                        count.append(2)
                    else:
                        count.append(5)
            case 6:
                if center in number:
                    if right[0] in number and right[1] in number:
                        count.append(9)
                    else:
                        count.append(6)
                else:
                    count.append(0)
            case 7:
                count.append(8)
    value = 0
    for i in range(len(count)):
        value += count[i] * 10 ** (len(count) - i - 1)
    sum+=value
    print(value)
print(sum)
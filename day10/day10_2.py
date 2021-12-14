file1 = open('input.txt', 'r')
lines = file1.readlines()
output = []
i=0
while i in range(len(lines)):
    expectedChar = []
    execute = False
    for char in lines[i]:
        match char:
            case '(':
                expectedChar.append(')')
                continue
            case '[':
                expectedChar.append(']')
                continue
            case '{':
                expectedChar.append('}')
                continue
            case '<':
                expectedChar.append('>')
                continue
        if char != '\n' and char != expectedChar[-1]:
            print("Error: expected ", expectedChar[-1], " found ", char)
            execute = True
            break
        elif char == expectedChar[-1]:
            expectedChar.pop()
    if execute:
        del lines[i]
    else:
        j=len(expectedChar)-1
        lines[i] = lines[i][:-1]
        new_output = 0
        while j >= 0:
            lines[i] = lines[i] + expectedChar[j]
            new_output = new_output * 5
            match expectedChar[j]:
                case ')':
                    new_output += 1
                case ']':
                    new_output += 2
                case '}':
                    new_output += 3
                case '>':
                    new_output += 4
            j-=1
        lines[i] = lines[i] + "\n"
        output.append(new_output)
        i+=1

output.sort()
print(output[len(output)//2])
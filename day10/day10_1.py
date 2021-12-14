file1 = open('input.txt', 'r')
lines = file1.readlines()

output = 0
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
            match char:
                case ')':
                    output += 3
                case ']':
                    output += 57
                case '}':
                    output += 1197
                case '>':
                    output += 25137
            execute = True
            break
        else:
            expectedChar.pop()
    if execute:
        del lines[i]
    else:
        i+=1

print(output)
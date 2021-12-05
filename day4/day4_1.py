def check_rows(board):
    for i in range(0, len(board)):
        for j in range(0, len(board)):
            if board[i][j][1] == False:
                break
            if j == len(board) - 1:
                return True
    return False

def check_columns(board):
    for i in range(0, len(board)):
        for j in range(0, len(board)):
            if board[j][i][1] == False:
                break
            if j == len(board) - 1:
                return True
    return False

file = open('input.txt', 'r')
input = file.readlines()

numbers=input[0].split(',')
iNumbers=[]
for data in numbers:
    iNumbers.append(int(data))

boards=[]
newBoard=[]
lineCount=0
for i in range(1, len(input)):
    if input[i] != '\n':
        line = (input[i].split())
        newBoard.append([])
        for j in range(0, len(line)):
            newBoard[lineCount].append([])
            newBoard[lineCount][j].append(int(line[j]))
            newBoard[lineCount][j].append(False)
        lineCount+=1
        if lineCount == 5:
            boards.append(newBoard.copy())
            newBoard.clear()
            lineCount=0

result=0
for number in iNumbers:
    for board in boards:
        for i in range(0, len(board)):
            for j in range(0, len(board[i])):
                if board[i][j][0] == number:
                    board[i][j][1] = True
        
        if check_rows(board) == True or check_columns(board) == True:
            sum=0
            for i in range(0, len(board)):
                for j in range(0, len(board[i])):
                    if board[i][j][1] == False:
                        sum += board[i][j][0]
            result=sum*number
        if result != 0:
            break
    if result != 0:
        break
print(result)
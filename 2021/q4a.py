import sys

def callnum(num, board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == num:
                board[i][j] = None

def won(board):
    for i in range(len(board)):
        won = True
        for j in range(len(board[0])):
            if board[i][j] is not None:
                won = False
        if won:
            return True
    for j in range(len(board[0])):
        won = True
        for i in range(len(board)):
            if board[i][j] is not None:
                won = False
        if won:
            return True

def left(board):
    ans = 0
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] is not None:
                ans += board[i][j]
    return ans

def work(nums, boards):
    for num in nums:
        for board in boards:
            callnum(num, board)
        for board in boards:
            if won(board):
                return left(board)*num

x = []
boards = []
for line in sys.stdin:
    x.append(line.strip())

nums = list(map(int,x[0].split(',')))
for i in range((len(x)-1)//6):
    board = []
    for j in range(5):
        board.append(list(map(int,x[i*6+j+2].split())))
    boards.append(board)

print(work(nums, boards))

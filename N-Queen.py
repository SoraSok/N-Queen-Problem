print ("Hello user, welcome to the N-Queen problem solver!", "How many queens do you want to place on the board?", sep = "\n")
n = int(input("Enter the number of queens: "))
if 1 < n < 4:
    print("There is no solution for", n, "queens.")
elif n == 1:
    print("There is only one queen on the board.")
    print("[Q]")
else:
    print("Solving the N-Queen problem...")
    def solution(board):
        for i in range(n):
            for j in range(n):
                print (board[i][j], end = ' ')
            print()

    def safe(board, row, column):
        for j in range(column):
            if board[row][j] == "Q":
                return False
        i, j = row, column
        while i >= 0 and j >= 0:
            if board[i][j] == "Q":
                return False
            i -= 1
            j -= 1
        i, j = row, column
        while i < n and j >= 0:
            if board[i][j] == "Q":
                return False
            i += 1
            j -= 1
        return True

    def place(board, column):
        if column == n:
            solution(board)
            return True
        print("Trying to place queen in column", column)
        print("Current board state:")
        solution(board)
        print()
        for i in range(n):
            if safe(board, i, column):
                board[i][column] = "Q"
                if place(board, column + 1) == True:
                    return True
                board[i][column] = "."
        return False

    def solve():
        board = [["." for _ in range(n)] for _ in range(n)]
        if place(board, 0) == False:
            print("There is no solution for", n, "queens.")
        else:
            print("Solution found!")

    solve()
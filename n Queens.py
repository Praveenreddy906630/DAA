def print_board(board):
    for row in board:
        print(" ".join("Q" if x else "." for x in row))
    print()

def is_safe(board, row, col, N):
    # Check this column on upper side
    for i in range(row):
        if board[i][col]:
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if j < 0: break
        if board[i][j]:
            return False

    # Check upper diagonal on right side
    for i, j in zip(range(row, -1, -1), range(col, N)):
        if j >= N: break
        if board[i][j]:
            return False

    return True

def solve_n_queens_util(board, row, N):
    if row >= N:
        print_board(board)
        return True

    res = False
    for col in range(N):
        if is_safe(board, row, col, N):
            board[row][col] = True
            res = solve_n_queens_util(board, row + 1, N) or res
            board[row][col] = False  # Backtrack

    return res

def solve_n_queens(N):
    board = [[False] * N for _ in range(N)]
    if not solve_n_queens_util(board, 0, N):
        print("No solution exists")

# Example usage
if __name__ == "__main__":
    N = int(input("Enter the number of queens (N): "))
    solve_n_queens(N)

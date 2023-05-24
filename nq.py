def issafe(arr, x, y, n):
    # Check if the current position is safe for the queen

    # Check the column for any other queens
    for row in range(x):
        if arr[row][y] == 1:
            return False

    row = x
    col = y
    # Check the upper diagonal on the left side
    while row >= 0 and col >= 0:
        if arr[row][col] == 1:
            return False
        row -= 1
        col -= 1

    row = x
    col = y
    # Check the upper diagonal on the right side
    while row >= 0 and col < n:
        if arr[row][col] == 1:
            return False
        row -= 1
        col += 1

    return True


def nQueen(arr, x, n):
    # Recursive function to solve the N-Queens problem

    if x >= n:
        # Base case: If all queens are placed, return True
        return True

    for col in range(n):
        if issafe(arr, x, col, n):
            # If it is safe to place a queen at the current position, mark it as 1
            arr[x][col] = 1

            if nQueen(arr, x + 1, n):
                # Recursive call to place the queens in the next row
                return True

            # If the recursive call does not lead to a solution, backtrack by marking the current position as 0
            arr[x][col] = 0

    return False


def main():
    n = int(input("Enter number of Queens: "))
    arr = [['x' for _ in range(n)] for _ in range(n)]  # Create an empty chessboard of size N x N

    if nQueen(arr, 0, n):
        # If the N-Queens problem is solvable, print the board configuration
        for i in range(n):
            for j in range(n):
                if arr[i][j] == 1:
                    print('Q', end=' ')  # Print 'Q' for queens
                else:
                    print('x', end=' ')  # Print 'x' for empty cells
            print()

if __name__ == '__main__':
    main()

def solve_n_queens(n):
    

    def backtrack(row):
        if row == n:
            solution = []
            for i in range(n):
                row_format = ['.'] * n
                row_format[board[i]] =  'Q'
                solution.append(''.join(row_format))
            result.append(solution)

        for col in range(n):
            major_diag = row - col + n - 1
            minor_diag = row + col

            if cols[col] or diag[major_diag] or anti_diag[minor_diag]:
                continue

            board[row] = col
            cols[col] = True
            diag[major_diag] = True
            anti_diag[minor_diag] = True

            backtrack(row + 1)

            cols[col] = False
            diag[major_diag] = False
            anti_diag[minor_diag] = False

    result = []
    board = [-1] * n
    cols = [False] * n
    diag = [False] * (2*n-1)
    anti_diag = [False] * (2*n-1)

    backtrack(0)
    return result

n = 4
res = solve_n_queens(n)
print(res)
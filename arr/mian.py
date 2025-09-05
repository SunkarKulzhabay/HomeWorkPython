#task1
n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]
max_value = matrix[0][0]
max_row, max_col = 0, 0
for i in range(n):
    for j in range(m):
        if matrix[i][j] > max_value:
            max_value = matrix[i][j]
            max_row, max_col = i, j
print(max_row, max_col)




#task1
n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]
max_value = matrix[0][0]
max_row, max_col = 0, 0
for i in range(n):
    for j in range(m):
        if matrix[i][j] > max_value:
            max_value = matrix[i][j]
            max_row, max_col = i, j
print(max_row, max_col)





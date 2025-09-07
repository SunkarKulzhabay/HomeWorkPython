# #task 1
# n, m = map(int, input().split())
# max_val = -1
# row, col = 0, 0
# for i in range(n):
#     line = input().strip()
#     for j in range(m):
#         num = int(line[j])
#         if num > max_val:
#             max_val = num
#             row, col = i, j
# print(row, col)
# #task 2
# n = int(input())
# array = [[0 for _ in range(n)] for _ in range(n)]
# for i in range(n):
#     for j in range(n):
#         array[i][j] = "."
# for j in range(n):
#     array[n//2][j] = "*"
# for j in range(n):
#     array[j][n//2] = "*"
# for j in range(n):
#     array[j][j] = "*"
# for j in range(n):
#     array[j][n - 1 - j] = "*"
# for row in array:
#     print(" ".join(row))
# #task 3
# n = int(input())
# m = int(input())
# array = [[0 for _ in range(n)] for _ in range(m)]
# for i in range(m):
#     for j in range(n):
#         if (i+j) % 2 == 0:
#             array[i][j] = "."
#         else:
#             array[i][j] = "*"
# for row in array:
#     print(" ".join(row))
#task 4
n = int(input())
m = int(input())
array = [[0 for _ in range(n)] for _ in range(m)]
for i in range(m):
    for j in range(n):
        array[i][j] = int(input())
def SwapColumns(A, i, j):
    for h in range(n):
        for w in range(n):
            if A[h][w] == A[i][w] or A[h][w] == A[j][w]:
                l = A[h][w]
n = int(input())
m = int(input())
array = [[0 for _ in range(n)] for _ in range(m)]
for i in range(m):
    for j in range(n):
        array[i][j] = int(input())
def SwapColumns(A, i, j):
    for h in range(n):
        for w in range(n):
            if A[h][w] == A[i][w] or A[h][w] == A[j][w]:
                l = A[h][w]





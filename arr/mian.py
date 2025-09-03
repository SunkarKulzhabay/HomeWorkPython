#task1
row = int(input())
cols = int(input())
matrix = []
for i in range(row):
    row = []
    for j in range(cols):
        value = int(input(f"Введите элемент [{i}][{j}]: "))
        row.append(value)
    matrix.append(row)


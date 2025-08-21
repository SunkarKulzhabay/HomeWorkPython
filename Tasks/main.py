# #Задача 1
# A = 179
# B = 971
# C = (A**2) + (B**2)
# print(C)
# #Задача 2
# D = 109
# V = float(input())
# T = float(input())
# C = V * T
# print(C)
# #Задача 3
# A = int(input())
# print(A%10)
# #Задача 4
# A = int(input())
# print(int(A/10))
# #Задача 5
# N = int(input())
# print((N+2 - N%2))
# #Задача 2
# D = 109
# V = int(input())
# T = int(input())
# position = (V * T) % D
# print(position)
# #Задача 6
# import math
# from re import match
#
# A = int(input('A: '))
# B = int(input('B: '))
# C = int(input('C: '))
# D = int(input('D: '))
# A = math.ceil(A/2)
# B = math.ceil(B/2)
# C = math.ceil(C/2)
# D = math.ceil(D/2)
# A = (A + 1) // 2
# B = (B + 1) // 2
# C = (C + 1) // 2
# D = (D + 1) // 2
# print(A + B + C + D)
# #Задача 7
# N = int(input())
# O = (N // 60) % 24
# print(O)
# K = N % 60
# print(K)
# print(f'{O}:{K}')
# #Задача 8
# N = int(input())
# O = (N // 3600) % 24
# K = (N // 60) % 60
# S = N % 60
# print(f'{O}:{K:02}:{S:02}')
# #Задача 9
# a = int(input())
# b = int(input())
# print(f'a: {a}')
# print(f'b: {b}')
# temp = a
# a = b
# b = temp
# print(f'a: {a}')
# print(f'b: {b}')
# #Задача 10
# a = int(input())
# b = int(input())
# print(f'a: {a}')
# print(f'b: {b}')
# a = a + b
# b = a - b
# a = a - b
# print(f'a: {a}')
# print(f'b: {b}')
# #Задача 11
n = 600
a = int(input('введите число от 1 до 10: '))
for i in range(2, a+1):


k = (n // 60) % 24
b = (n % 60)
print(f'{k:02}:{b:02}')






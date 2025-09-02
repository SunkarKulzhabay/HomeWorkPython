# #task1
# def powr(a,n):
#     count = 0
#     for i in range(n+1):
#         count = a ** i
#     print(count)
#
# powr(2,1)
# #task2
# def gcd(a: int, b: int) -> int:
#     if b == 0:
#         return a
#     return gcd(b, a % b)
#
# def reduceFraction(n: int, m: int) -> tuple[int, int]:
#     d = gcd(n, m)
#     return (n // d, m // d)
# print(reduceFraction(12, 16))
# #task3
# def IsPrime(x):
#     if x % 2 != 0 and x % 3 != 0 and x % 5 != 0:
#         print("Yes")
#     elif x == 2 or x == 5 or x == 3:
#         print("Yes")
#     else:
#         print("No")
# IsPrime(2)
# IsPrime(4)
# #task4
# def rec(a,n):
#     if n == 0:
#         return 1
#     return a * rec(a, n-1)
# print(rec(2,3))
# #task5
# def sum(a, b):
#     if b == 0:
#         return a #точка выхда
#
#     return sum(a+1 , b - 1) # вход 2 в цикл
# sum(2,2)
# print(sum(4,4)) # вход 1
# #task6
# def phib(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return phib(n-1) + phib(n-2)
# print(phib(6))



# # #task1
# # def powr(a,n):
# #     if n == 0:
# #         return 1
# #     if n == 1:
# #         return a
# #     return a*pow(a,n-1)
# #
# # print(powr(2,3))
# # #task2
# # def gcd(a: int, b: int) -> int:
# #     if b == 0:
# #         return a
# #     return gcd(b, a % b)
# #
# # def reduceFraction(n: int, m: int) -> tuple[int, int]:
# #     d = gcd(n, m)
# #     return (n // d, m // d)
# # print(reduceFraction(12, 16))
# # #task3
# # def IsPrime(x):
# #     if x % 2 != 0 and x % 3 != 0 and x % 5 != 0:
# #         print("Yes")
# #     elif x == 2 or x == 5 or x == 3:
# #         print("Yes")
# #     else:
# #         print("No")
# # IsPrime(2)
# # IsPrime(4)
# # #task4
# # def rec(a,n):
# #     if n == 0:
# #         return 1
# #     return a * rec(a, n-1)
# # print(rec(2,3))
# # #task5
# # def sum(a, b):
# #     if b == 0:
# #         return a #точка выхда
# #
# #     return sum(a+1 , b - 1) # вход 2 в цикл
# # sum(2,2)
# # print(sum(4,4)) # вход 1
# # #task6
# # def phib(n):
# #     if n == 0:
# #         return 0
# #     elif n == 1:
# #         return 1
# #     else:
# #         return phib(n-1) + phib(n-2)
# # print(phib(6))
# # #task7
# # sud = 0
# # def sub(sud=0):
# #     a = int(input())
# #     if a == 0:
# #         return sud
# #     return sub(sud + a)
# # print(sub(sud))
# # #task8
# # def sub():
# #     a = int(input())
# #     if a == 0:
# #         print(0)
# #         return
# #     sub()
# #     print(a)
# # sub()
#
#
# # # task6
# # dub = list()
# # n = input()
# # index = 0
# # while n != 'stop':
# #     dub.append(int(n))
# #     n = input()
# # temp = dub[0]
# # for i in range(1, len(dub)):
# #     if dub[i] > temp:
# #             temp = dub[i]
# #             index = i
# # print(temp, index)
#
# # #Если ввести 1 2 3 4 выдает некорректный ответ
#
# # #task7
# # dub = list()
# # n = input()
# # temp = None
# # while n != 'stop':
# #     dub.append(int(n))
# #     n = input()
# # for i in range(len(dub) - 1):
# #     if dub[i] % 2 != 0:
# #             if temp is None or dub[i] < temp:
# #                 temp = dub[i]
# # if temp is None:
# #  print(0)
# # else:
# #     print(temp)
#
# # #task9
# # dub = list()
# # n = input()
# # temp1i = 0
# # temp2i = 0
# # while n != 'stop':
# #     dub.append(int(n))
# #     n = input()
# # for i in range(len(dub)):
# #     temp1 = dub[0]
# #     temp2 = dub[0]
# #     if temp1 > dub[i]:
# #         temp1 = dub[i]
# #         temp1i = i
# #     if temp2 < dub[i]:
# #         temp2 = dub[i]
# #         temp2i = i
# # dub[temp1i] = temp2
# # dub[temp2i] = temp1
# # print(dub)
#
# # #task10
# # dub = list()
# # gun = dict()
# # n = input()
# # temp = 0
# # while n != 'stop':
# #     dub.append(int(n))
# #     n = input()
# # for i in dub:
# #     if i in gun:
# #         gun[i] += 1
# #     else:
# #         gun[i] = 1
# # for key, value in gun.items():
# #     if value == 1:
# #         print(key)
#
# # #если ввести 1 2 2 3 3 3 4 выводится только 1 а должен 1 4
#
# #task11
# dub = []
# n = input()
#
# while n != 'stop':
#     dub.append(int(n))
#     n = input()
#
# max_count = 0
# max_g = None
#
# for i in range(len(dub)):
#     current_count = dub.count(dub[i])
#     if current_count > max_count:
#         max_count = current_count
#         max_g = dub[i]
#
# print(max_g, " ", max_count)
#
# # # Сейчас вы ищите только подряд идущие элементы. А должно работать и для всех одинаковых чисел списка.
#
#
#
#
#
#
#
#
#
#
#
#
#
#

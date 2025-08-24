# # Task 1
# a = int(input())
# b = int(input())
# if a > b:
#     print(1)
# elif a == b:
#     print(0)
# elif a < b:
#     print(2)
#
# # Task 2
# x = int(input())
# if x > 0:
#     print(1)
# elif x < 0:
#     print(-1)
# else:
#     print(0)
#
# # Task 3
# a = int(input())
# if a % 4 == 0 and a % 100 != 0 or a % 400 == 0:
#     print("Yes")
# else:
#     print("No")
# # Task 4
# a = int(input())
# b = int(input())
# c = int(input())
# if a + b >= c and a + c >= b and b + c >= a:
#     print('Yes')
# else:
#     print('No')
# # Task 5
# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())
# if a == c or b == d:
#     print("True")
# else:
#     print("False")
# # Task 6
# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())
# if abs(a - c) <= 1 and abs(b - d) <= 1 and (a != c or b != d):
#     print("YES")
# else:
#     print("NO")
# # Task 7
# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())
# if abs(a - c) == abs(b - d):
#     print("Yes")
# else:
#     print("No")
# Task 8
# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())
# if (((a + b) % 2 == 0) == ((c + d) % 2 == 0)) or (((a + b) % 2 != 0) == ((c + d) % 2 != 0)):
#     print("Yes")
# else:
#     print("No")
# #Task 9
# n = int(input())
# if n == 1:
#     print(f'{n} korova')
# elif n >= 2 and n <= 4:
#     print(f'{n} korovy')
# else:
#     print(f'{n} korov')
# #Task 10
# n = int(input())
# a = 0
# b = 0
# c = 0
# c  = n // 60
# n = n % 60
# if n <= 8:
#     a = n
# elif n <= 30:
#     b = n // 10
#     n = n % 10
#     if n % 10 != 0:
#         if n == 9:
#             b += 1
#         else:
#             a = n % 10
# else:
#     c += 1
# print(f'{a}:{b}:{c}')
# #Task 11
# k = int(input())
# m = int(input())
# n = int(input())
# m = m * 2
# b = n // k
# c = n % k
# print(m * (b+c))














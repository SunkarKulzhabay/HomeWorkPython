# #task1
# def chis(n):
#     if n == 0:
#         return n
#     chis(n - 1)
#     print(n)
# print(chis(5))x
# #task2
# def ub(a,b):
#     if a == b:
#         print(a)
#     elif a < b:
#         print(a, end=" ")
#         ub(a+1, b)
#     else:
#         print(a, end=" ")
#         ub(a-1, b)
# ub(1,5)
#task3
# def A(m,n):
#     if m == 0:
#        return n+1
#     elif n == 0 and m > 0:
#         return A(m-1, 1)
#     elif m > 0 and n > 0:
#         return A(m-1,A(m,n-1))
# print(A(2,2))

# def E(n):
#     if n==1:
#         print("Yes")
#     elif n % 2 != 0 or n == 0:
#         print("No")
#     else:
#         E(n//2)
# E(8)
# b = 0
# def u(n):
#      if n < 10:
#          return n
#      else:
#          return n % 10 + u(n // 10)
# u(179)
# print(u(179))

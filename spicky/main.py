# #task1
# dub = list()
# n = input()
# while n != 'stop':
#     dub.append(int(n))
#     n = input()
# for i in range (len(dub)):
#     if i % 2 == 0:
#         print(dub[i])
# #task2
# dub = list()
# n = input()
# while n != 'stop':
#     if int(n) % 2 == 0:
#         dub.append(int(n))
#     n = input()
# print(dub)
# #task3
# dub = list()
# n = input()
# count = 0
# while n != 'stop':
#     dub.append(int(n))
#     n = input()
# for i in range(len(dub)):
#     if dub[i] >= 0:
#         count += 1
# print(count)
# #task4
# dub = list()
# n = input()
# while n != 'stop':
#     dub.append(int(n))
#     n = input()
# for i in range (len(dub)-1):
#     if dub[i] < dub[i+1]:
#         print(dub[i+1])
# #task5
# dub = list()
# n = input()
# count = 0
# while n != 'stop':
#     dub.append(int(n))
#     n = input()
# for i in range (len(dub)-2):
#     if dub[i] < dub[i+1] and dub[i+1] > dub[i+2]:
#         count += 1
# print(count)
# #task6
# dub = list()
# n = input()
# temp = 0
# index = 0
# while n != 'stop':
#     dub.append(int(n))
#     n = input()
# for i in range(len(dub)-1):
#     if dub[i] > dub[i+1]:
#         if temp is None or dub[i] > temp:
#             temp = dub[i]
#             index = i
# print(temp, index)
# #task7
# dub = list()
# n = input()
# temp = None
# while n != 'stop':
#     dub.append(int(n))
#     n = input()
#
# for i in range(len(dub) - 1):
#     if dub[i] % 2 != 0:
#         if dub[i] < dub[i+1]:
#             if temp is None or dub[i] < temp:
#                 temp = dub[i]
# print(temp)
# #task8
# dub = list()
# n = input()
# temp = None
# count = 0
# while n != 'stop':
#     dub.append(int(n))
#     n = input()
# for i in range(len(dub) - 1):
#     if temp != dub[i]:
#         temp = dub[i]
#         count += 1
# print(count)
#task9
dub = list()
n = input()
temp1 = None
temp2 = None
while n != 'stop':
    dub.append(int(n))
    n = input()
for i in range(len(dub) - 1):
    if temp1 > dub[i]:
        temp = dub[i]
        count += 1
print(count)


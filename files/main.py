# #task1
# myFile = open('myFile.txt','r')
# text = myFile.read()
# result = text.split()
# result = [int(x) for x in result]
# print(sum(result))
# #task2
# myFile = open('myFile.txt','w')
# text = myFile.write('hello world\n')
# myFile.close()
# myFile = open('myFile.txt','r')
# text1 = myFile.read()
# text1 = text1.rstrip()
# print(text1[::-1])
# #task3
# myFile = open('myFile.txt','r')
# text = myFile.read().split('\n')
# for line in reversed(text):
#     print(line)
# #task4
# lines = 0
# spaces = 0
# words = 0
# myFile = open('myFile.txt','r')
# for line in myFile:
#     lines += 1
#     spaces += line.count(' ')
#     words += len(line.split())
# print(lines)
# print(spaces)
# print(words)

# Beautiful is better than ugly.
# Explicit is better than implicit.
# Simple is better than complex.
# Complex is better than complicated.

# #task5
# scores = {'A': [], 'B': [], 'C': []}
# with open('myFile.txt', 'r', encoding='utf-8') as myFile:
#     for line in myFile:
#         parts = line.split()
#         klass = parts[-2]  # класс (A/B/C)
#         score = int(parts[-1])  # балл
#         scores[klass].append(score)
# result = []
# for klass in ['A', 'B', 'C']:
#     if scores[klass]:
#         avg = sum(scores[klass])/len(scores[klass])
#     else:
#         avg = 0
#     result.append(avg)
# print(*result)
# Иванов Сергей A 80
# Амикул Нурай B 91
# Амраев Ильяс C 82
# Булатова Амина A 93
# Сембиев Алдияр A 64
# Сергеева Ирина B 50






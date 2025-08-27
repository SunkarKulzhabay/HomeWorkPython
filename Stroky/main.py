# #Task 1
# stroka = 'Abrakadabra'
# print(stroka[2])
# print(stroka[-2])
# print(stroka[0:5])
# print(stroka[0::2])
# print(stroka[1::2])
# print(stroka[::-2])
# print(len(stroka))
# #Task 2
# from os.path import split
# tag = 'Hello world'
# print(len(split(tag)))
# #Task 3
# stg = str(input())
# mid = (len(stg) + 1)//2
# stg1 = stg[:mid]
# stg2 = stg[mid:]
# print(stg2 + stg1)
# #Task 4
# text = 'In the hole in the ground there lived a hobbit'
# text1 = text.lower()
# a = text1.find('h')
# b = text1.find('h',a+1)
# print(text[:a] + text[b:] )
# #Task 5
# n = 'Bilbo.Baggins@bagend.hobbiton.shire.me'
# print(n.replace('@',''))
#Task 6
n = 'python'
for i in range(len(n)):
    if n[i]%3==0:
        n = n.replace(i,n)
    else:
        continue
print(n)





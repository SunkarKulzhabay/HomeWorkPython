#Задача 1
A = 179
B = 971
C = (A**2) + (B**2)
print(C**(1/2))
#Задача 2
D = 109
V = float(input())
T = float(input())
C = V * T
print(C)
#Задача 3
A = int(input())
print(A%10)
#Задача 4
A = int(input())
print(int(A/10))
#Задача 5
N = int(input())
print((N+2 - N%2))
#Задача 2
D = 109
V = int(input())
T = int(input())
position = (V * T) % D
print(position)
#Задача 6 тут было два варианта решение с и без библиотеки

A = int(input('A: '))
B = int(input('B: '))
C = int(input('C: '))
D = int(input('D: '))

A = (A + 1) // 2
B = (B + 1) // 2
C = (C + 1) // 2
D = (D + 1) // 2
print(A + B + C + D)
#Задача 7
N = int(input())
O = (N // 60) % 24
print(O)
K = N % 60
print(K)
print(f'{O}:{K}')
#Задача 8
N = int(input())
O = (N // 3600) % 24
K = (N // 60) % 60
S = N % 60
print(f'{O}:{K:02}:{S:02}')
#Задача 9
a = int(input())
b = int(input())
print(f'a: {a}')
print(f'b: {b}')
temp = a
a = b
b = temp
print(f'a: {a}')
print(f'b: {b}')
#Задача 10
a = int(input())
b = int(input())
print(f'a: {a}')
print(f'b: {b}')
a = a + b
b = a - b
a = a - b
print(f'a: {a}')
print(f'b: {b}')
#Задача 11
n = 600 + 55
a = int(input("Введите число от 1 до 10: "))
if 1 <= a <= 10:
    for i in range(2, a+1):
        if i % 2 == 0:
            n += 70
        else:
            n += 80
    k = (n // 60) % 24
    y = n % 60
    print(f"{k:02}:{y:02}")
else:
    print("Ошибка! Введите число от 1 до 10")
#Задача 12
a = int(input())
b = int(input())
n = int(input())
m = 0
d = 0
if b * n > 100:
    m = (b * n) / 100
    d = int((b * n) % 100)
    a = a * n
    print(f'{a + m} : {d}')
else:
    print(f'{a * n} : {b * n}')

#Задача 13
h1 = int(input())
m1 = int(input())
s1 = int(input())
print('------------------------------')
h2 = int(input())
m2 = int(input())
s2 = int(input())

h1 = h1 * 60 ** 2
h2 = h2 * 60 ** 2
m1 = m1 * 60
m2 = m2 * 60
s1 = h1 + m1 + s1
s2 = h2 + m2 + s2
print('------------------------------')
print(abs(s2 - s1))

#Задача 14
n = int(input())
k = int(input())
m = k//n
if k % n != 0:
    m = m + 1
print(m)
#Задача 15
h = int(input())
a = int(input())
b = int(input())
c = 0
d = 0
while True:
    d += 1
    c = c + a
    if c >= h:
        print(d)
        break
    c = c - b
#Задача 16
n = int(input())
m = int(input())
if n % m == 0 or m % n == 0:
    print(1)
else:
    print(0)
#Задача 1
A = 179
B = 971
C = (A**2) + (B**2)
print(C**(1/2))
#Задача 2
D = 109
V = float(input())
T = float(input())
C = V * T
print(C)
#Задача 3
A = int(input())
print(A%10)
#Задача 4
A = int(input())
print(int(A/10))
#Задача 5
N = int(input())
print((N+2 - N%2))
#Задача 2
D = 109
V = int(input())
T = int(input())
position = (V * T) % D
print(position)
#Задача 6 тут было два варианта решение с и без библиотеки

A = int(input('A: '))
B = int(input('B: '))
C = int(input('C: '))
D = int(input('D: '))

A = (A + 1) // 2
B = (B + 1) // 2
C = (C + 1) // 2
D = (D + 1) // 2
print(A + B + C + D)
#Задача 7
N = int(input())
O = (N // 60) % 24
print(O)
K = N % 60
print(K)
print(f'{O}:{K}')
#Задача 8
N = int(input())
O = (N // 3600) % 24
K = (N // 60) % 60
S = N % 60
print(f'{O}:{K:02}:{S:02}')
#Задача 9
a = int(input())
b = int(input())
print(f'a: {a}')
print(f'b: {b}')
temp = a
a = b
b = temp
print(f'a: {a}')
print(f'b: {b}')
#Задача 10
a = int(input())
b = int(input())
print(f'a: {a}')
print(f'b: {b}')
a = a + b
b = a - b
a = a - b
print(f'a: {a}')
print(f'b: {b}')
#Задача 11
n = 600 + 55
a = int(input("Введите число от 1 до 10: "))
if 1 <= a <= 10:
    for i in range(2, a+1):
        if i % 2 == 0:
            n += 70
        else:
            n += 80
    k = (n // 60) % 24
    y = n % 60
    print(f"{k:02}:{y:02}")
else:
    print("Ошибка! Введите число от 1 до 10")
#Задача 12
a = int(input())
b = int(input())
n = int(input())
m = 0
d = 0
if b * n > 100:
    m = (b * n) / 100
    d = int((b * n) % 100)
    a = a * n
    print(f'{a + m} : {d}')
else:
    print(f'{a * n} : {b * n}')

#Задача 13
h1 = int(input())
m1 = int(input())
s1 = int(input())
print('------------------------------')
h2 = int(input())
m2 = int(input())
s2 = int(input())

h1 = h1 * 60 ** 2
h2 = h2 * 60 ** 2
m1 = m1 * 60
m2 = m2 * 60
s1 = h1 + m1 + s1
s2 = h2 + m2 + s2
print('------------------------------')
print(abs(s2 - s1))

#Задача 14
n = int(input())
k = int(input())
m = k//n
if k % n != 0:
    m = m + 1
print(m)
#Задача 15
h = int(input())
a = int(input())
b = int(input())
c = 0
d = 0
while True:
    d += 1
    c = c + a
    if c >= h:
        print(d)
        break
    c = c - b
#Задача 16
n = int(input())
m = int(input())
if n % m == 0 or m % n == 0:
    print(1)
else:
    print(0)
#Задача 1
A = 179
B = 971
C = (A**2) + (B**2)
print(C**(1/2))
#Задача 2
D = 109
V = float(input())
T = float(input())
C = V * T
print(C)
#Задача 3
A = int(input())
print(A%10)
#Задача 4
A = int(input())
print(int(A/10))
#Задача 5
N = int(input())
print((N+2 - N%2))
#Задача 2
D = 109
V = int(input())
T = int(input())
position = (V * T) % D
print(position)
#Задача 6 тут было два варианта решение с и без библиотеки

A = int(input('A: '))
B = int(input('B: '))
C = int(input('C: '))
D = int(input('D: '))

A = (A + 1) // 2
B = (B + 1) // 2
C = (C + 1) // 2
D = (D + 1) // 2
print(A + B + C + D)
#Задача 7
N = int(input())
O = (N // 60) % 24
print(O)
K = N % 60
print(K)
print(f'{O}:{K}')
#Задача 8
N = int(input())
O = (N // 3600) % 24
K = (N // 60) % 60
S = N % 60
print(f'{O}:{K:02}:{S:02}')
#Задача 9
a = int(input())
b = int(input())
print(f'a: {a}')
print(f'b: {b}')
temp = a
a = b
b = temp
print(f'a: {a}')
print(f'b: {b}')
#Задача 10
a = int(input())
b = int(input())
print(f'a: {a}')
print(f'b: {b}')
a = a + b
b = a - b
a = a - b
print(f'a: {a}')
print(f'b: {b}')
#Задача 11
n = 600 + 55
a = int(input("Введите число от 1 до 10: "))
if 1 <= a <= 10:
    for i in range(2, a+1):
        if i % 2 == 0:
            n += 70
        else:
            n += 80
    k = (n // 60) % 24
    y = n % 60
    print(f"{k:02}:{y:02}")
else:
    print("Ошибка! Введите число от 1 до 10")
#Задача 12
a = int(input())
b = int(input())
n = int(input())
m = 0
d = 0
if b * n > 100:
    m = (b * n) / 100
    d = int((b * n) % 100)
    a = a * n
    print(f'{a + m} : {d}')
else:
    print(f'{a * n} : {b * n}')

#Задача 13
h1 = int(input())
m1 = int(input())
s1 = int(input())
print('------------------------------')
h2 = int(input())
m2 = int(input())
s2 = int(input())

h1 = h1 * 60 ** 2
h2 = h2 * 60 ** 2
m1 = m1 * 60
m2 = m2 * 60
s1 = h1 + m1 + s1
s2 = h2 + m2 + s2
print('------------------------------')
print(abs(s2 - s1))

#Задача 14
n = int(input())
k = int(input())
m = k//n
if k % n != 0:
    m = m + 1
print(m)
#Задача 15
h = int(input())
a = int(input())
b = int(input())
c = 0
d = 0
while True:
    d += 1
    c = c + a
    if c >= h:
        print(d)
        break
    c = c - b
#Задача 16
n = int(input())
m = int(input())
if n % m == 0 or m % n == 0:
    print(1)
else:
    print(0)











































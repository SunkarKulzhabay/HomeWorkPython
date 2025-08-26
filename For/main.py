#task 1
n = int(input())
a = 1
b = 0
while True:
    b = (pow(a,2))
    if b > n:
        break
    print(b)
    a += 1
#task 2
n = int(input())
a = 2
while True:
    if n % a != 0:
        a += 1
    else:
        print(a)
        break
#task 3
n = int(input())
a = 1
if n == 0:
    print(1)
else:
    for i in range(1,n+1):
        a = a * i
    print(a)
#task 4
n = int(input())
a = 0
for i in range(1, n):
    b = (i * (i+1))
    a += b
print(a)
#task 5
n = int(input())
a = 0
for i in range(n):
    i = int(input())
    a += i
print(a)
# или второй вариант
n = int(input())
print(sum(int(input()) for _ in range(n)))
#task 6
n = int(input())
a = 0
for i in range(n):
    i = int(input())
    if(i==0):
        a += 1
print(a)
#task 7 я не правильно понял задачу
n = int(input())
list1 = []
for _ in range(n):
    x = int(input())
    if x < 100:
        print('Нужно больше 100')
        continue
    if sum(int(d) for d in str(x)) == 3:
        list1.append(x)
print(sorted(list1))
n = int(input())
for x in range(100, 1000):
    if sum(int(d) for d in str(x)) == n:
        print(x, end=" ")
#task 8
n = int(input())
x = 1
f = 0
for i in range(1,n + 1):
    x *= i
    f += x
print(f)
#task 9
n = int(input())
sum1 = 0
sum2 = 0
for i in range(1,n):
    sum1 += i
    j = int(input())
    sum2 += j
print((sum1 + n) - sum2)
#task 10
n = int(input())
print((n//100)+((n // 10)%10)+(n % 10))
print(sum(int(d) for d in str(n)))
#task 11
n  = int(input())
if n < 1000:
    b = (n // 100)
    c = (n // 10) % 10
    d = n % 10
    if 0 == d and b == c:
        print(1)
    else:
        print(0)
else:
    a = n // 1000
    b = (n // 100) % 10
    c = (n // 10) % 10
    d = n % 10
    if a == d and b == c:
        print(1)
    else:
        print(0)










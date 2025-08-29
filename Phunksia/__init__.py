#task 1
def pov(a,n):
    if a == n:
        return 1
    return a * pov(a, n - 1)
print(pov(2,3))












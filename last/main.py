#task 1
print(len(set(input().split()) & set(input().split())))
#task 2
n = int(input())
m = int(input())
langs = {input().strip() for _ in range(m)}
common = langs.copy()
all_langs = langs.copy()
for _ in range(n - 1):
    m = int(input())
    langs = {input().strip() for _ in range(m)}
    common &= langs
    all_langs |= langs
print(len(common))
for lang in sorted(common):
    print(lang)
print(len(all_langs))
for lang in sorted(all_langs):
    print(lang)


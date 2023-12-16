n = int(input())
for i in range(n):
    s = input()
    if 'кот' in s:
        index = s.index('кот') + 1
        print(i + 1, index)


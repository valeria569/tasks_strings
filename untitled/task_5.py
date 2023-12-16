N = int(input())
advices = []


for _ in range(N):
    advice = input()
    advices.append(advice)

for advice in advices:
    if advice.startswith("не ") or advice.startswith("Не "):
        print(advice[3:])
    else:
        print(advic)

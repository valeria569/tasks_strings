def count_bulls_and_cows(word1, word2):
    bulls = 0
    cows = 0

    for i in range(len(word1)):
        if word1[i] == word2[i]:
            bulls += 1
        elif word1[i] in word2:
            cows += 1

    return bulls, cows

word1 = input("Введите первое слово: ")
word2 = input("Введите второе слово: ")

result = count_bulls_and_cows(word1, word2)
print(f"{result[0]} {result[1]}")

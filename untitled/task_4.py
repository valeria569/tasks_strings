words = []
while True:
    word = input()
    if word == 'стоп':
        break
    words.append(word)

shortest_word = min(words, key=len)
longest_word = max(words, key=len)

if set(shortest_word).issubset(set(longest_word)):
    print('ДА')
else:
    print('НЕТ')

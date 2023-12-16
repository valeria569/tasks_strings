max_length = int(input("Введите максимальную длину анонса: "))
num_titles = int(input("Введите количество заголовков: "))

titles = []
for _ in range(num_titles):
    title = input("Введите заголовок: ")
    titles.append(title)

print("Результат:")
for title in titles:
    if len(title) <= max_length:
        print(title)
    else:
        shortened_title = title[:max_length-3] + "..."
        print(shortened_title)

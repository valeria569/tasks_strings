import re

def check_username(username):
    pattern = r'^[A-Za-z0-9_]+$'
    if re.match(pattern, username):
        return "OK"
    else:
        invalid_char = re.search(r'[^a-z0-9_]', username).group()
        return f"Неверный символ: {invalid_char}"

username = input("Введите имя пользователя: ")
result = check_username(username)
print(result)

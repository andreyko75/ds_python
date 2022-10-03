# Дополните её код таким образом, чтобы возникала ошибка ValueError с текстом "Invalid Mark!"
# при попытке поставить оценку не из списка: 2, 3, 4 или 5.

def add_mark(name, mark, journal=None):
    # Добавьте здесь проверку аргумента mark
    if mark not in range(2, 6, 1):
        raise (ValueError("Invalid Mark!"))
    if journal is None:
        journal = {}
    journal[name] = mark
    return journal


# попытка вызвать функцию с некорректными аргументами
try:
    print(add_mark('Ivanov', 6))
# должна завершиться с ошибкой ValueError, которую мы выведем в блоке except
except ValueError as e:
    print(e)

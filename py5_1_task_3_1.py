def get_time(distance, speed):
    # Добавьте проверку скорости на равенство 0
    # Верните ошибку ValueError с текстом
    # "Speed cannot be equal to 0!"

    if distance < 0 or speed < 0:
        raise ValueError("Distance or speed cannot be below 0!")
    if speed == 0:
        raise ValueError("Speed cannot be equal to 0!")
    result = distance / speed
    return result


# попытка вызвать функцию с некорректными аргументами
try:
    print(get_time(100, 0))
# должна завершиться с ошибкой ValueError, которую мы выведем в блоке except
except ValueError as e:
    print(e)

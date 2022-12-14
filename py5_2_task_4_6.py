# Напишите функцию is_leap(year), которая принимает на вход год и возвращает
# True, если год високосный, иначе — False.
# Условие для проверки на високосность: год делится на 400 или год делится на 4,
# но не на 100. Подробнее об этом можно узнать здесь.
# Пример работы функции:
# print(is_leap(2000))
# print(is_leap(1900))
# print(is_leap(2020))
# # True
# # False
# # True
def is_leap(year):
    return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)


print(is_leap(1900))

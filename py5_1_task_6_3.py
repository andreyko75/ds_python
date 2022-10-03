# Напишите lambda-функцию для расчёта гипотенузы прямоугольного треугольника:
# она принимает на вход длины двух катетов и возвращает длину гипотенузы
# (третьей, самой длинной стороны прямоугольного треугольника).
# Формула: c=(a**2+b**2)**(1/2), где a и b — длины катетов, c — длина гипотенузы.
# Сохраните эту функцию в переменную hyp.
# пример:
# print(hyp(3,4))
# print(hyp(1,9))
# # 5.0
# # 9.055385138137417
hyp = lambda a, b: (a ** 2 + b ** 2) ** (1 / 2)
print(hyp(3, 4))
print(hyp(1, 9))

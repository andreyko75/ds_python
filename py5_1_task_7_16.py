# Перепишите функцию between_min_max из задания 7.12 в lambda-функцию.
# Функция принимает на вход числа через запятую и возвращает одно число —
# среднее между максимумом и минимумом этих чисел.
#
# Пример:
#
# print(between_min_max(1,2,3,4,5))
# # 3.0


between_min_max = lambda *args: (min(args) + max(args)) / 2
print(between_min_max(1, 2, 3, 4, 5))

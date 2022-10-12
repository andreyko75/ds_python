# Усложним предыдущую задачу.

# Напишите функцию sum_min_numbers(), которая также принимает три числа на вход
# и возвращает сумму двух наименьших.
# Можно использовать функцию из предыдущего задания для поиска минимального числа.

from functools import reduce


def sum_min_numbers(a, b, c):
    numb_list = [a, b, c]
    min_1 = reduce(lambda x, y: x if x < y else y, numb_list)
    numb_list.remove(min_1)
    return min_1 + numb_list[0] if numb_list[0] < numb_list[1] else min_1 + numb_list[1]


print(sum_min_numbers(0, 0, 0))

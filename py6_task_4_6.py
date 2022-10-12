# Напишите функцию def even_numbers_in_matrix(),
# которая получает на вход матрицу (список из списков)
# и возвращает количество четных чисел в ней.
from functools import reduce

matrix_example = [
    [1, 5, 4],
    [4, 2, -2],
    [7, 65, 88]
]


def even_numbers_in_matrix(matrix):
    matrix_new = reduce(lambda a, b: a + b, matrix)
    return sum(True for i in matrix_new if i % 2 == 0)


print(even_numbers_in_matrix(matrix_example))

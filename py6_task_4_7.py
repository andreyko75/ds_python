# Напишите функцию def matrix_sum(), которая получает на вход две матрицы
# и возвращает их сумму.
# Примечание: чтобы найти сумму двух матриц, нужно просуммировать
# их соответствующие элементы. Но перед этим необходимо проверить, что размеры
# матриц одинаковы (одинаковое количество столбцов и одинаковое количество строк)
# Например:
# 1 2 3   2 3 4   3 5 7
# 2 3 4 + 4 5 6 = 6 8 10
# 5 6 7   4 3 2   9 9 9
from functools import reduce

matrix_example = [
    [1, 5, 4],
    [4, 2, -2],
    [7, 65, 88]
]


def matrix_sum(matrix1, matrix2):
    matrix_new1 = reduce(lambda a, b: a + b, matrix1)
    matrix_new2 = reduce(lambda a, b: a + b, matrix2)
    if len(matrix1) != len(matrix2) or len(matrix_new1) != len(matrix_new2):
        return None
    result = [[matrix1[i][j] + matrix2[i][j] for j in range(len(matrix1[0]))] for i in range(len(matrix1))]
    return result


print(matrix_sum(matrix_example, matrix_example))

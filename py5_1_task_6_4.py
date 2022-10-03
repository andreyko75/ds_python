# Напишите функцию sort_sides, которая сортирует переданный в неё список.
# Входной список состоит из кортежей с парами чисел — длинами катетов прямоугольных треугольников.
# Функция должна возвращать список, отсортированный по возрастанию длин гипотенуз треугольников.
# print(sort_sides([(3,4), (1,2), (10,10)]))
# # [(1, 2), (3, 4), (10, 10)]

# hyp = lambda a, b: (a ** 2 + b ** 2) ** (1 / 2)

def sort_sides(l_in):
    hyp_up = []
    hyp_up_sort = []
    print(l_in)
    for i in l_in:
        hyp = lambda a, b: (a ** 2 + b ** 2) ** (1 / 2)
        hyp_up.append((hyp(i[0], i[1]), i[0], i[1]))
    hyp_up.sort()
    for i in hyp_up:
        hyp_up_sort.append((i[1], i[2]))
    return hyp_up_sort


sort_sides([(1, 2), (3, 4), (10, 10)])

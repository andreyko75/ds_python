# Напишите рекурсивную функцию multiply_lst, которая перемножает элементы заданного списка между собой.

def multiply_lst(lst):
    if len(lst) == 0:
        return 1
    return lst[0] * multiply_lst(lst[1:])


my_lst = [10, 21, 24, 12]
print(multiply_lst(my_lst))

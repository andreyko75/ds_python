# Напишите функцию sort_ignore_case, которая принимает на вход список и сортирует его без учёта регистра по алфавиту.
#
# Функция возвращает отсортированный список.
#
# Пример:
#
# print(sort_ignore_case(['Acc', 'abc']))
# # ['abc', 'Acc']
def sort_ignore_case(ls):
    return (sorted(ls, key=str.lower))


print(sort_ignore_case(['Acc', 'abc']))

# Напишите небольшую программу, которая реализует ввод
# произвольного количества чисел через пробел и выводит эти же самые числа построчно.

# Пример:
# входные данные:
# 1 2 3 4 5 6 7
# вывод:
# 1
# 2
# 3
# 4
# 5
# 6
# 7

# Примечание для продвинутых программистов:
# попробуйте решить задачу без использования циклов.
gen_string = input('Enter string ')
# gen_string='1 2 3 4 5 6 7'
split_string = gen_string.split()
print('\n'.join(split_string))
# В цикле добавляйте в список cut_str_list списки, состоящие из порядкового номера строки из списка str_list (номер в
# рамках данной задачи начинается от 0) и 3 первых символа из каждой строки. Если длина строки меньше Трёх символов,
# то добавляется вся строка целиком. В результате работы вашей программы в переменной cut_str_list должен храниться
# результирующий вложенный список.

str_list = ["Hello", "my", "name", "is", "Ezeikel", "I", "like", "knitting"]  # заданный список
cut_str_list = []  # задаем новый список

# ваш код здесь
count_char = 0
for i in str_list:
    cut_str_list.append([count_char, i[:3]])
    count_char += 1
print(cut_str_list)

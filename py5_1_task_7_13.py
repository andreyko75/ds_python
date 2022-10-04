# Напишите функцию best_student(...), которая принимает на вход в виде именованных аргументов
# имена студентов и их номера в рейтинге (нагляднее в примере).
#
# Необходимо вернуть фамилию студента с минимальным номером по рейтингу.
#
# Пример:
#
# print(best_student(Tom=12, Mike=3))
# print(best_student(Tom=12))
# print(best_student(Tom=12, Jerry=1, Jane=2))
# # Mike
# # Tom
# # Jerry
def best_student(**qwargs):
    min_val = min(qwargs.values())
    for key, val in qwargs.items():
        if min_val == val:
            return key


print(best_student(Tom=12, Jerry=1, Jane=2))

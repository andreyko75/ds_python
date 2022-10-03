# Напишите функцию is_prime(num), которая проверяет, является ли число простым.
#
# Функция должна вернуть True, если число простое, иначе — False.
#
# Примечание. Простым называют число, которое делится только на 1 или на само себя. Число 1 простым не является.
#
# Пример:
#
# print(is_prime(1))
# print(is_prime(10))
# print(is_prime(13))
# # False
# # False
# # True
def is_prime(num):
    if num==1:
        return False
    if num==2:
        return True
    i=round(num**(1/2))
    while i>1:
        if i%num==0:
            return False
        print (i,num)
        return True
        num-=1


print(is_prime(2))

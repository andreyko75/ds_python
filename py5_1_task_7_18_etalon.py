# *Задание повышенной сложности
#
# Напишите функцию exchange(usd, rub, rate),
# которая может принимать на вход сумму в долларах (usd), сумму в рублях (rub)
# и обменный курс (rate). Обменный курс показывает, сколько стоит один доллар.
# Например, курс 85.46 означает, что один доллар стоит 85 рублей и 46 копеек.
#
# В функцию должно одновременно передавать два аргумента. Если передано менее
# двух аргументов, должна возникнуть ошибка ValueError('Not enough arguments').
# Если же передано три аргумента, должна возникнуть ошибка: ValueError('Too many arguments').
#
# Функция должна находить третий аргумент по двум переданным. Например, если переданы суммы в
# разных валютах, должен возвращаться обменный курс. Если известны сумма в рублях и курс,
# должна быть получена эквивалентная сумма в долларах, аналогично — если передана сумма в долларах и обменный курс.
#
# Пример:
#
# print(exchange(usd=100, rub=8500))
# print(exchange(usd=100, rate=85))
# print(exchange(rub=1000, rate=85))
# # 85.0
# # 8500
# # 11.764705882352942
# print(exchange(rub=1000, rate=85, usd=90))
# # ValueError: Too many arguments
# print(exchange(rub=1000))
# # ValueError: Not enough arguments

def exchange(usd=None, rub=None, rate=None):
    check = [usd, rub, rate].count(None)
    check_lst = ['Too many arguments', None, 'Not enough arguments']
    if check != 1: raise ValueError(check_lst[check])
    if usd is None:
        usd = rub / rate
        return usd
    if rub is None:
        rub = usd * rate
        return rub
    if rate is None:
        rate = rub / usd
        return rate

print(exchange(usd=100, rate=85))

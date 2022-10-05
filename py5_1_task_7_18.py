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

def exchange(**qwargs):
    if len(qwargs) == 1:
        raise ValueError('Not enough arguments')
    elif len(qwargs) == 3:
        raise ValueError('Too many arguments')
    rub_get = qwargs.get('rub', qwargs.get('rate', 1) * qwargs.get('usd', 1))
    usd_get = qwargs.get('usd', qwargs.get('rub', 1) / qwargs.get('rate', 1))
    rate_get = qwargs.get('rate', qwargs.get('rub', 1) / qwargs.get('usd', 1))
    return (rub_get + usd_get + rate_get - sum(qwargs.values()))


print(exchange(rub=1000, rate=85))



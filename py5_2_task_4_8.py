# Представьте, что вы пишете приложение, предусматривающее регистрацию пользователей.
# Давайте реализуем небольшой функционал регистрации. Не забудем также про «проверку на дурака».
#
# Напишите функцию register(surname, name, date, middle_name, registry).
#
# Функция имеет следующие аргументы:
#
# surname — фамилия;
# name — имя;
# date — дата рождения (в виде кортежа из трёх чисел — день, месяц, год);
# middle_name — отчество ;
# registry — список, в который необходимо добавить полученные аргументы в виде кортежа
# в следующем порядке: фамилия, имя, отчество, день, месяц, год рождения.
# Функция должна возвращать список, в который добавила запись.
#
# Указание: сделайте отчество аргументом по умолчанию со значением None,
# так как отчество может быть не у всех регистрирующихся.
#
# Также сделайте так, чтобы пустой список создавался в том случае, если он не был передан извне.
# Таким образом, по умолчанию registry имеет значение None, и если при вызове функции список не был
# передан, он создаётся в теле функции.
#
# Наконец, проверьте дату на корректность. Если дата неправильная, верните ошибку
# ValueError("Invalid Date!"). Для этого вам пригодится функция check_date из предыдущего задания.
#
ddef register(surname, name, date, middle_name=None, registry=None):

    def check_date(day, month, year):
        tru_date = []
        d_days = {1: 31, 2: 28 + (year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)), 3: 31, 4: 30, 5: 31, 6: 30,
                  7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
        tru_date.append(year >= 1900 and year <= 2022)
        tru_date.append(type(day * month * year) is int)
        tru_date.append(month >= 1 and month <= 12)
        tru_date.append(day >= 1 and day <= d_days.get(month, 0))
        return True if tru_date.count(True) == 4 and isinstance(date,tuple) else False

    day, month, year = date
    if check_date(day, month, year) == False: raise ValueError('Invalid Date!')
    if registry == None: return [(surname, name, middle_name, day, month, year)]
    reg.append((surname, name, middle_name, day, month, year))
    return registry

reg=[]
reg = register('Petrova', 'Maria', (13, 12, 2003), 'Ivanovna')
reg = register('Ivanov', 'Sergej', (24, 9, 1995), registry=reg)
reg = register('Smith', 'John', (13, 2, 2003), registry=reg)
print(reg)

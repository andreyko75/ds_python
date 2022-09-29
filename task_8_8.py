##
# Напишите программу, которая выводит на экран фразу в формате:
# Hello, <name>! Today is <dayofweek>. Have a nice day!
# пример: "Hello, John! Today is Friday. Have a nice day!"
# информация о пользователе содержится в следующих переменных:
# name - имя пользователя, dayofweek - название дня недели
# ! обязательное условие - задача должна быть решена с использованием метода format
# ! Codeboard не поддерживает f-строки, поэтому используйте метод format()
name = 'John'
dayofweek = 'Friday'
# ваш код здесь
#print(f'Hello, {name}! Today is {dayofweek}. Have a nice day!')
print('Hello, {}! Today is {}. Have a nice day!'.format(name, dayofweek))

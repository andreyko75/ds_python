names = ['Ivan', 'Nikita', 'Simon', 'Margarita', 'Vasilisa', 'Kim']
# Отбираем имена из пяти и более букв
long_names = filter(lambda x: len(x) >= 5, names)
print(list(long_names))
# Все отобранные имена переводим в верхний регистр и считаем число букв А в них
# Результат сохраняем в виде кортежа (имя, число букв "A")
count_a = map(lambda x: [x, x.upper().count('A')], long_names)
# Переводим объект map в list и печатаем его

print(list(count_a))
text = '''
She sells sea shells on the sea shore;
The shells that she sells are sea shells I am sure.
So if she sells sea shells on the sea shore,
I am sure that the shells are sea shore shells.
'''
text = text.lower()  # приводим текст к нижнему регистру
text = text.replace(" ", "")  # заменяем пробелы на пустые строки
text = text.replace("\n", "")  # заменяем символы переноса строки на пустые строки
count_dict = {}  # создаём пустой словарь для подсчёта количества символов
# создаём цикл по символам в строке text
for symbol in text:  # symbol — текущий символ в тексте
    # проверяем условие, что символа ещё нет среди ключей словаря
    if symbol not in count_dict:  # если условие выполняется,
        count_dict[symbol] = 1  # заносим символ в словарь со значением 1
    else:  # в противном случае
        count_dict[symbol] += 1  # увеличиваем частоту символа
print(count_dict)  # выводим результирующий словарь
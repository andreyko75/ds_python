# Олег положил тысячу рублей в банк под 8% годовых. Через сколько лет у него на счету будет не менее трёх тысяч
# рублей? Выведите на экран это число и запишите его в ответ.
o_money, i = 1000, 0
while o_money <= 3000:
    o_money *= 1.08
    i += 1
print(o_money, i)




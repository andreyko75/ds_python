reg = [('Ivanov', 'Sergej', 24, 9, 1995),
       ('Smith', 'John', 13, 2, 2003),
       ('Petrova', 'Maria', 13, 3, 2003)]

# ваш код здесь
new_reg = list(map(lambda y: (y[0] + ' ' + y[1][0] + '.', y[2], y[3], y[4]), filter(lambda x: x[-1] >= 2000, reg)))

print(new_reg)

# Создайте цикл, позволяющий понять, через сколько секунд босс убьёт вашего персонажа. В результате работы в
# переменной second_num должно быть сохранено количество секунд, в течение которых будет длиться схватка.
current_health = 500  # заданный показатель здоровья
attack = 80  # заданная атака босса
seconds_num = 0  # задаем начальное время схватки
while current_health > 0:
    current_health -= attack
    seconds_num += 1
print(current_health, seconds_num)
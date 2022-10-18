# Напишите функцию task_manager, которая принимает список задач для нескольких серверов.
# Каждый элемент списка состоит из кортежа (<номер задачи>, <название сервера>, <высокий приоритет задачи>).
#
# Функция должна создавать словарь и заполнять его задачами по следующему принципу:
# название сервера — ключ, по которому хранится очередь задач для конкретного сервера.
# Если поступает задача без высокого приоритета (последний элемент кортежа — False),
# добавить номер задачи в конец очереди. Если приоритет высокий, добавить номер в начало.
#
# Для словаря используйте defaultdict, для очереди — deque.
#
# Функция возвращает полученный словарь с задачами.
# defaultdict(, {'voltage': deque([41667, 35364]),
# 'office': deque([36871, 40690, 33850])})
from collections import deque,OrderedDict,Counter,defaultdict
tasks = [(36871, 'office', False),
         (40690, 'office', False),
         (35364, 'voltage', False),
         (41667, 'voltage', True),
         (33850, 'office', False)]
def task_manager(tasks):
    tasks = sorted(tasks, key=lambda x: x[2], reverse=True)
    d=defaultdict(deque)
    for x, y, z in tasks:
        d[y].append((x))
    for y,x in d.items():
        print()
        z=deque(x)
        d[y].clear()
        d[y].append(z)
    d=sorted(d.items())
    print (d)
    return(d)
---








print(task_manager(tasks))

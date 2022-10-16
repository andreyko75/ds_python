
from collections import deque
def brackets(line):
    c=deque(line)
    c_temp=deque([True])

    #отсекаем если нечетное количество скобок
    if len(c)%2!=0:
        return False
    #отсекаем если пусто
    elif len(c)==0:
        return True
    c_temp.append(c.pop())
    while True:
        c_element=c.pop()
        if c_temp[-1] ==c_element:
            c_temp.append(c_element)
        else:c_temp.popleft()
        if len(c)==0:
            if len(c_temp)==1:
                return True
            else:return False


print(brackets("(()())"))

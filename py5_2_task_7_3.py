def logger(name):
    def decorated_func(*args, **kwargs):
        # Получаем время на момент начала вычисления
        print(name._name_),': Function root started'
        result = func(*args, **kwargs)
        # Получаем время на момент окончания вычисления
        end = time()
        # Считаем длительность вычисления
        delta = end - start
        # Печатаем время работы функции
        print("Runtime:", delta)
        return result
    return decorated_func

# @time_decorator
# def root(value, n=2):
#     result = value ** (1 / n)
#     return result


@logger('MainLogger')
def root(val, n=2):
    res = val ** (1 / n)
    return res


print(root(25))
# MainLogger: Function root started
# MainLogger: Function root finished
# 5.0
wswswdx

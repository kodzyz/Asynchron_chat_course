"""Простейший декоратор-класс"""


class Log():
    def __init__(self):
        pass

    # Магический метод __call__ позволяет обращаться к объекту класса, как к функции
    """Класс-декоратор"""

    def __call__(self, func):
        def decorated(*args, **kwargs):
            """Обертка"""
            res = func(*args, **kwargs)
            print(f'log: {func.__name__}({args}, {kwargs}) = {res}')
            return res

        return decorated


@Log()
def my_func(val_1, val_2):
    """Вычисление"""
    return val_1 ** val_2


print('-- Функции с декораторами --')
# my_func = Log()(my_func)
my_func(4, 5)

# другой подход применения декоратора к функции func2 = Log()(func2)
# func2 = Log()(func2)
# func2(4, 5)

# ---------терминал
# -- Функции с декораторами --
# log: my_func((4, 5), {}) = 1024

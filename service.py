# 0:50 генератор

# python3 service.py

from functools import wraps


class Log:
    def __int__(self):
        pass

    def __call__(self, func):  # __call__ срабатывает при вызове класса
        @wraps(func)
        def wrapper(*args, **kwargs):
            print(f'Вызов {func.__name__} {args} {kwargs}')
            # ... до выполнения основной ф-и
            r = func(*args, **kwargs)
            # ... после выполнения основной ф-и
            print(f'{func.__name__} вернула {r}')
            return r

        # wrapper.__doc__ = func.__doc__
        print('doctest wrapper', wrapper.__doc__)

        return wrapper


@Log()
def square(x):
    """ Вычисляет квадрат
        >>> square(4):
        16
    """
    print('Идет выполнение задачи...')
    return x * x


square(4)

# doctest wrapper  Вычисляет квадрат
#         >>> square(4):
#         16
#
# Вызов square (4,) {}
# Идет выполнение задачи...
# square вернула 16

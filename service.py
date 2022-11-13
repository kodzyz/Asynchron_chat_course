# 0:37 декоратор с параметром

# python3 service.py
class Log:
    def __int__(self):
        pass

    def __call__(self, func):  # __call__ срабатывает при вызове класса
        def wrapper(*args, **kwargs):
            print(f'Вызов {func.__name__} {args} {kwargs}')
            # ... до выполнения основной ф-и
            r = func(*args, **kwargs)
            # ... после выполнения основной ф-и
            print(f'{func.__name__} вернула {r}')
            return r

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
print(square.__doc__)

# Идет выполнение задачи...
#  Вычисляет квадрат
#         >>> square(4):
#         16

from functools import wraps

# Декоратор @wraps(func), объявленный в модуле functools,
# копирует атрибуты функции func в атрибуты обернутой версии функции.
# Атрибуты функции сохраняются в словаре, доступном в виде __dict__.


def wrap(func):
    @wraps(func)
    def call(*args, **kwargs):
        r = func(*args, **kwargs)
        print(f'{func.__name__} вернула {r}')
        return r

    print(f'1. doctest wrapper {func.__doc__}')
    print(f'2. name: {func.__name__}')
    print(f'3. {func.__module__}')
    print(f'4. {func.__annotations__}')
    print(f'5. {func.__qualname__}')

    return call


@wrap
def factorial(n):
    """ Вычисляет факториал числа n. Например:
    >>> factorial(6)
    120
    """
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)

factorial(5)
# 0:30 несколько декораторов

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


def level1(func):
    def wrapper(*args, **kwargs):
        print('deep 1')
        r = func(*args, **kwargs)
        print('deep 1 end')
        return r

    return wrapper


def level2(func):
    def wrapper(*args, **kwargs):
        print('deep 2')
        r = func(*args, **kwargs)
        print('deep 2 end')
        return r

    return wrapper


def level3(func):
    def wrapper(*args, **kwargs):
        print('deep 3')
        r = func(*args, **kwargs)
        print('deep 3 end')
        return r

    return wrapper


@level1
@level2
@level3
def square(x):
    print('Идет выполнение задачи...')
    return x * x


square(4)

# deep 1
# deep 2
# deep 3
# Идет выполнение задачи...
# deep 3 end
# deep 2 end
# deep 1 end

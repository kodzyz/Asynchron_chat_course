# 0:30 декоратор в виде класса с магик методом

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


@Log()  # декоратор класса пишется в скобках
def square(x):
    print('Идет выполнение задачи...')
    return x * x


square(4)


# Вызов square (4,) {}
# Идет выполнение задачи...
# square вернула 16

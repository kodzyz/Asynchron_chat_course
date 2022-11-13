# 0:24

# python3 service.py

def trace(func):
    def wrapper(*args, **kwargs):
        print(f'Вызов {func.__name__} {args} {kwargs}')
        # ... до выполнения основной ф-и
        r = func(*args, **kwargs)
        # ... после выполнения основной ф-и
        print(f'{func.__name__} вернула {r}')
        return r

    return wrapper


@trace  # ф-я обертка - декоратор
def square(x):
    print('Идет выполнение задачи...')
    return x * x


square(4)


# Вызов square (4,) {}
# Идет выполнение задачи...
# square вернула 16

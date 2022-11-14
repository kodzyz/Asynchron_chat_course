# Декоратор с параметрами # 1:05

import time
from functools import wraps


def sleep(timeout):
    def decorator(func):
        @wraps(func)
        def decorated(*args, **kwargs):
            ''' Декоратор sleep '''
            t1 = time.sleep(timeout)
            res = func(*args, **kwargs)
            print('Function {} was sleeping'.format(func.__name__))
            return res

        return decorated

    return decorator


@sleep(2)  # ф-я декоратор будет вызываться при каждом цикле рекурсии
def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(5))

# -----терминал через 10 секунд
#  python3 04_deco_params.py
# Function factorial was sleeping
# Function factorial was sleeping
# Function factorial was sleeping
# Function factorial was sleeping
# Function factorial was sleeping
# 120
# python3 01_deco.py

# trace() создает функцию-обертку,
# которая записывает отладочную информацию в
# файл и затем вызывает оригинальный объект функции.

enable_tracing = True
if enable_tracing:
    debug_log = open("debug.log", "w")


def trace(func):
    if enable_tracing:
        def callf(*args, **kwargs):
            debug_log.write(f"{func.__name__}, {args}, {kwargs}\n")
            r = func(*args, **kwargs)
            debug_log.write(f"{func.__name__} вернула {r}\n")
            #return r

        return callf
    else:
        return func


@trace  # square = trace(square)
def square(x):
    return x * x


square(4)

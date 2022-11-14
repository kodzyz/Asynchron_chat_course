# Когда выполняется декоратор c.8

# Главное свойство декораторов —
# они выполняются сразу после определения декорируемой функции,
# обычно на этапе импорта (когда Python загружает модуль).

registry = []  # Список-реестр «зарегистрированных» функций


def register(func):
    ''' Декоратор, регистрирующий функции в неком "реестре" '''
    print(' running register ( %s ) ' % func)
    registry.append(func)
    print(registry)
    return func


# Функции, которые могут быть декорированы:
@register
def f1():
    print('running f1()')


@register
def f2():
    print('running f2()')


# Намеренно декорируем не все функции
def f3():
    print('running f3()')


def main():
    print(' running main()')
    # Выведем список «зарегистрированных» функций
    print(' registry ->', registry)

    # Теперь просто выполним все функции
    f1()
    f2()
    f3()

# if __name__ == '__main__':
#     main()


# -----терминал
# python3 when_deco_is_called.py

# running register ( <function f1 at 0x7f47af481c10> )
# [<function f1 at 0x7f47af481c10>]
# running register ( <function f2 at 0x7f47af481ca0> )
# [<function f1 at 0x7f47af481c10>, <function f2 at 0x7f47af481ca0>]

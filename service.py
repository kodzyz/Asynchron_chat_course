# ф-я для теста
def get_params():
    return (1, 'config')


# вариант теста 1
def test_get_params():
    if get_params() == (1, 'config'):
        print('Test passed')
    else:
        print('Test not passed')


# вариант теста 2
def test_get_params1():
    print('Test passed') if get_params() == (1, 'config') else print('Test not passed')


# вариант теста 3
# оператор 'assert' для сравнения правой и левой части, возвращает True или False
def test_get_params2():
    assert get_params() == (1, 'config')  # (2, 'config') -> False -> # AssertionError


test_get_params()
test_get_params1()
test_get_params2()

# вариант использования 'assert' вместо 'if...else'
admin = False


def get_params1():
    if admin:
        return (1, 'config')
    return '403'


def get_params2():
    assert admin == True  # если части равны то пропускаем дальше, если нет то ошибка
    return (1, 'config')  # admin = False -> AssertionError


get_params2()

import datetime
from collections import namedtuple

Salary = namedtuple('Salary', ('surname', 'name', 'worked', 'rate'))


def get_salary(line):
    ''' Вычисление зарплаты работника '''
    line = line.split()
    if line:
        data = Salary(*line)
        fio = ' '.join((data.surname, data.name))
        salary = int(data.worked) * int(data.rate)
        res = (fio, salary)
    else:
        res = ()
    return res


def test_get_salary_summ():
    assert get_salary('Лютиков    Руслан   60  1000') == \
           ('Лютиков Руслан', 60000), 'Неверная сумма математики'


def test_get_salary_fio():
    assert get_salary('Лютиков    Руслан   60  1000')[0] == 'Лютиков Руслан', 'Неверное имя филологи'


def test_get_salary_empty():
    assert get_salary('') == (), 'Непустые данные'


def test_get_salary_wrong_format():
    assert get_salary(' ') == (), 'Непустые данные'


if __name__ == "__main__":
    test_get_salary_fio()
    test_get_salary_summ()
    test_get_salary_empty()
    test_get_salary_wrong_format()

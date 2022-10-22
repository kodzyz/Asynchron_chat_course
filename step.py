import sys
import argparse

# python3 step.py
# python3 step.py -n Вася
# python3 step.py --name Вася


def createParser():
    parser = argparse.ArgumentParser()  # экземпляр класса ArgumentParser
    parser.add_argument('-n', '--name')  # добавили ожидаемый параметр в командной строке (nargs='?')- необязательный
    return parser


if __name__ == '__main__':
    parser = createParser()
    namespace = parser.parse_args(sys.argv[1:])  # метод 'parse_args' для разбора командной строки

    print(namespace)
    # Namespace(name=None)
    # Namespace(name='Вася')
    # Namespace(name='Вася')

    print(f'Привет, {namespace.name}!')  # name=None! # Привет, Вася!



import sys
import argparse

# python3 step.py #  python3 step.py kostya

def createParser():
    parser = argparse.ArgumentParser()  # экземпляр класса ArgumentParser
    parser.add_argument('name', nargs='?', default='мир')  # добавили ожидаемый параметр в командной строке (nargs='?')- необязательный
    return parser


if __name__ == '__main__':
    parser = createParser()
    namespace = parser.parse_args(sys.argv[1:])  # метод 'parse_args' для разбора командной строки

    print(namespace)  # Namespace(name='мир') # Namespace(name='kostya')

if namespace.name:
    print(f'Привет, {namespace.name}!')  # Привет, мир! # Привет, kostya!



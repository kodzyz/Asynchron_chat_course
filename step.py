import sys
import argparse


def createParser():
    parser = argparse.ArgumentParser()  # экземпляр класса ArgumentParser
    parser.add_argument('name', nargs='?')  # добавили ожидаемый параметр в командной строке (nargs='?')- необязательный
    return parser


if __name__ == '__main__':
    parser = createParser()
    namespace = parser.parse_args()  # метод 'parse_args' для разбора командной строки

    print(namespace)  # Namespace(name=None) # Namespace(name='kostya')

if namespace.name:
    print(f'Привет, {namespace.name}!')
else:
    print('Привет, мир!')

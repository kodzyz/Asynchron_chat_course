import sys
import argparse


# ожидает два позиционных параметра -
# имя приветствуемого человека и число,
# обозначающее, сколько раз его нужно поприветствовать.

# python3 step.py Петя 3


def createParser():
    parser = argparse.ArgumentParser()  # экземпляр класса ArgumentParser
    parser.add_argument('name')
    parser.add_argument('count', type=int)
    return parser


if __name__ == '__main__':
    parser = createParser()
    namespace = parser.parse_args(sys.argv[1:])  # метод 'parse_args' для разбора командной строки

    print(namespace)  # Namespace(count=3, name='Петя')

    for _ in range(namespace.count):
        print(f'Привет, {namespace.name}!')

        # Привет, Петя!
        # Привет, Петя!
        # Привет, Петя!

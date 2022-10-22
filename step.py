import sys
import argparse

# python3 step.py
# python3 step.py -n Вася
#


def createParser():
    parser = argparse.ArgumentParser()  # экземпляр класса ArgumentParser
    parser.add_argument('-n')
    return parser


if __name__ == '__main__':
    parser = createParser()
    namespace = parser.parse_args(sys.argv[1:])  # метод 'parse_args' для разбора командной строки

    print(namespace)
    # Namespace(n=None)
    # Namespace(n='Вася')


    print(f'Привет, {namespace.n}!')  # Привет, None! # Привет, Вася!



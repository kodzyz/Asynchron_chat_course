import sys
import argparse


# python3 step.py
# python3 step.py -n Вася
# python3 step.py -n Вася Оля Петя


def createParser():
    parser = argparse.ArgumentParser()  # экземпляр класса ArgumentParser
    parser.add_argument('-n', '--name', nargs='+', default=['мир'])  # nargs='+', ожидаем одно или более значение
    return parser


if __name__ == '__main__':
    parser = createParser()
    namespace = parser.parse_args(sys.argv[1:])  # метод 'parse_args' для разбора командной строки

    print(namespace)
    # Namespace(name=['мир'])
    # Namespace(name=['Вася'])
    # Namespace(name=['Вася', 'Оля', 'Петя'])

    for name in namespace.name:
        print(f'Привет, {name}!')

        # Привет, мир! # Привет, Вася!
        # Привет, Вася!
        # Привет, Оля!
        # Привет, Петя!



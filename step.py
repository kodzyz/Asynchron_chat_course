import sys
import argparse

# два позиционных параметра -
# сделаем их оба именованными,
# в этом случае порядок их передачи будет не важен

# python3 step.py --name Петя --count 3
# python3 step.py --count 3 --name Петя
# python3 step.py -c 3 -n Петя

def createParser():
    parser = argparse.ArgumentParser()  # экземпляр класса ArgumentParser
    parser.add_argument('-n', '--name')
    parser.add_argument('-c', '--count', type=int, default=1)
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

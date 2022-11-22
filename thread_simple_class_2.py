"""Отдельный класс-поток"""

import time
from threading import Thread


# thread_simple_1.py в виде класса:

# t.run() — вызывается при запуске потока.
# По умолчанию вызывает функцию target, которая
# была передана конструктору.
# Можно создать свой класс, производный от Thread, и
# определить в нем собственную реализацию метода run();


class ClockThread(Thread):  # объявляется собственный класс потока
    """Класс-наследник потока"""

    def __init__(self, interval):  # в котором переопределяется метод __init__()
        super().__init__()  # важно вызвать конструктор базового класса super().__init__()
        self.daemon = True  # True в атрибуте daemon позволяет интерпретатору завершиться сразу после выхода из главной программы
        self.interval = interval

    def run(self):
        while True:
            print(f"Текущее время: {time.ctime()}")
            time.sleep(self.interval)

    # Неверным будет и пытаться переопределить другие методы класса Thread,
    # кроме run() и __init__().


THR = ClockThread(1)
THR.start()
THR.join()

# Чтобы проследить работу потока после вызова метода t.start(), необходимо также добавить вызов
# метода t.join(). Иначе приложение завершится сразу после запуска потока.


# python3 thread_simple_class_2.py
# --------терминал
# while True

# Текущее время: Tue Nov 22 21:29:46 2022
# Текущее время: Tue Nov 22 21:29:47 2022
# Текущее время: Tue Nov 22 21:29:48 2022

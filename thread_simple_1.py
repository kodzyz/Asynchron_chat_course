"""Простой поток"""

# пример того, как создавать и запускать функции в
# отдельных потоках управления стр.6


import time
from threading import Thread


def clock(interval):
    """Функция, которая может быть запущена в потоке"""

    while True:
        print(interval)
        print(f"Текущее время: {time.ctime()}")
        time.sleep(interval)


# Thread(group=None, target=None, name=None, args=(), kwargs={})
THR = Thread(target=clock, args=(1,))  # clock(1)

"""
Обычно Python-приложение не завершается, пока работает хоть один его поток. 
Но есть особые потоки, которые не мешают закрытию программы и останавливается вместе с ней. 
Их называют демонами (daemons). Проверить, является ли поток демоном, можно методом isDaemon(). 
Если является, метод вернёт истину.
"""

THR.daemon = False  # атрибут класса: будет ли поток демоническим
THR.start()  # метод класса: запускает поток
THR.join()  # ожидает завершения потока

# python3 thread_simple_1.py
# --------терминал
# while True

# ...
# 1
# Текущее время: Tue Nov 22 21:18:49 2022
# ...

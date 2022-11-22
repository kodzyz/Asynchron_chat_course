"""Класс-поток"""

import time
import random
from threading import Thread


class MyThread(Thread):
    """Поток"""
    def __init__(self, name):
        """Инициализация потока"""
        super().__init__()
        self.name = name

    def run(self):
        """Запуск следующих команд в потоке"""
        amount = random.randint(3, 15)
        time.sleep(amount)
        msg = f"Поток {self.name} запущен"
        print(msg)


def create_threads():
    """Создаем группу потоков"""
    for i in range(5):
        name = f"Thread {i + 1}"
        my_thread = MyThread(name)
        # запуск потока
        my_thread.start()


if __name__ == "__main__":
    create_threads()

# python3 thread_simple_add_3.py
# --------терминал
# Поток Thread 2 запущен
# Поток Thread 4 запущен
# Поток Thread 3 запущен
# Поток Thread 1 запущен
# Поток Thread 5 запущен

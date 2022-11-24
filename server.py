"""Класс-процесс"""

import time
from multiprocessing import Process


class ClockProcess(Process):
    """Простой класс-процесс"""
    def __init__(self, interval):
        super().__init__()
        self.interval = interval

    def run(self):
        while True:
            print(f"Текущее время: {time.ctime()}")
            time.sleep(self.interval)


if __name__ == "__main__":
    PROC = ClockProcess(1)
    PROC.start()

# Текущее время: Thu Nov 24 00:06:55 2022
# Текущее время: Thu Nov 24 00:06:56 2022
# Текущее время: Thu Nov 24 00:06:57 2022

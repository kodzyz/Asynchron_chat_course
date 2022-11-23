"""
Обмен данными при помощи очередей
"""

from threading import Thread
from queue import Queue    


class WorkerThread(Thread):
    """Поток с очередью в классе"""
    def __init__(self, *args, **kwargs):  # обязательная ф-я
        super().__init__(*args, **kwargs)
        self.input_queue = Queue()  # объявление очереди: две функции - положить и забрать

    def send(self, item):
        """Положить объект в очередь"""
        self.input_queue.put(item)

    def close(self):
        """Закрыть очередь"""
        self.input_queue.put(None)  # положить = None, очередь close
        self.input_queue.join()  # блокирует соединение, пока все элементы в очереди не будут получены и обработаны

    def run(self):  # WT_OBJ.start()
        while True:
            item = self.input_queue.get()  # метод получает сообщение из очереди, потом удаляет
            if item is None:
                break
            # Обработать элемент
            # (замените инструкцию print какими-нибудь полезными операциями)
            print(item)  # если сообщение есть - печатаем
            self.input_queue.task_done()  # сообщает очереди, что обработка задачи завершена
        # Конец. Сообщить, что сигнальная метка была принята, и выйти
        self.input_queue.task_done()
        return


# Пример использования
WT_OBJ = WorkerThread()
WT_OBJ.start()
# Отправить элемент на обработку (с помощью очереди)
WT_OBJ.send("hello")
WT_OBJ.send("world")
WT_OBJ.close()

from threading import Thread, Lock

# обезопасим программы от гонки за ресурсом

def make_desicion():
    l = Lock()  # инит Lock
    l.acquire()  # на время использования файла блокируем все
    with open('text.txt', 'a') as f:
        f.write('hi its a second thread\n')
    l.release()  # отпускаем все процессы когда закончили работу с файлом


def write_to_file():
    l = Lock()
    l.acquire()
    with open('text.txt', 'a') as f:
        f.write('hello its a first thread\n')
    l.release()


t1 = Thread(target=write_to_file)
t2 = Thread(target=make_desicion)

t1.start()
t2.start()

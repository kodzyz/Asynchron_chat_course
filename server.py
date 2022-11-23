from threading import Thread, Lock
import time

# показано что блокировки не привязаны к конкретному потоку
# и мы блоктровку приобретенную в одном процессе отпускаем в другом

done = Lock()  # общая блокировка


def idle_release():
    print("Running release!")
    time.sleep(5)
    done.release()  # отпускаем блокировку которая приобреталась в основном потоке


done.acquire()  # приобретаем блокировку в основном потоке
Thread(target=idle_release).start()  # запустили 'idle_release'
done.acquire()  # приобретаем блокировку снова
print("Странное поведение мьютексов в Python...")


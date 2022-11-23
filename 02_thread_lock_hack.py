# Объекты класса Lock

from threading import Thread, Lock
import time

done = Lock()  # создает новый экземпляр блокировки, изначально находится в состоянии «открыто»


def idle_release():
    print("Running release!")
    time.sleep(5)
    done.release()  # lock.release() — освобождает блокировку


done.acquire()  # lock.acquire([blocking]) — приобретает блокировку.
Thread(target=idle_release).start()
done.acquire()
print("Странное поведение мьютексов в Python...")

# python3 02_thread_lock_hack.py
# Running release!
# Странное поведение мьютексов в Python...

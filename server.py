from threading import Thread, RLock
import time

#


done = RLock()  # рекурсивная блокировка


def idle_release():
    print("Running release!")
    time.sleep(5)
    done.release()


done.acquire()
done.acquire()
done.acquire()
done.acquire()
done.acquire()
done.release()
done.release()
Thread(target=idle_release).start()
done.acquire()
print(dir(done), done._is_owned(), done._release_save())
print("Странное поведение мьютексов в Python...")

# Running release!
# ['__class__', '__delattr__', '__dir__', '__doc__', '__enter__', '__eq__', '__exit__', '__format__',
# '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__',
# '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__',
# '__subclasshook__', '_acquire_restore', '_is_owned', '_release_save', 'acquire', 'release']
# True (4, 140612620945216)
# Странное поведение мьютексов в Python...
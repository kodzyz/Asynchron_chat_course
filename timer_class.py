# При работе с потоками
# рекомендуется организовать приложение как
# коллекцию независимых потоков,
# обменивающихся данными с помощью очередей сообщений

# Объекты класса Timer используются для вызова функций через определенное время.
# Создает объект таймера, который вызывает функцию
# func через interval секунд. В аргументах args и kwargs передаются позиционные и
# именованные аргументы для функции func. Таймер не запускается, пока не будет вызван
# метод start().

# Timer(interval, func [, args [, kwargs]])

# методы:
# t.start() — запускает таймер. Функция func, переданная конструктору Timer(), будет вызвана
# спустя указанное количество секунд после вызова этого метода;
# t.cancel() — останавливает таймер, если функция еще не была вызвана.


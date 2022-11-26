import os

# 1)
if not os.path.exists('test_dir'):  # проверка существования каталога:
    os.mkdir('test_dir')  # создание каталога

# 2) содержимое текущей директории
# python3
# >>> import os
# >>> dir_struct = os.listdir('.')
# >>> print(dir_struct)
# ['logs', 'venv', 'service.py', '.gitignore', 'main.py', '__pycache__', 'common', '.git', '.idea', 'test_dir']
# >>>

# 3) Проверка на объект-каталог
# >>> dirs = [d for d in os.listdir('.') if os.path.isdir(d)]  # 'True' если каталог существует
# >>> print(dirs)
# ['logs', 'venv', '__pycache__', 'common', '.git', '.idea', 'test_dir']
# >>>

# 4) Проверка на объект-файл 'path.isfile'
# >>> fls = [f for f in os.listdir('.') if os.path.isfile(f)]
# >>> print(fls)
# ['service.py', '.gitignore', 'main.py']
# >>>

# 5) Определение базового имени пути 'path.basename'
# >>> base_path = os.path.basename('/media/dk/Seagate Expansion Drive/Documents/GeekBrains/Python/Asynchron_chat/less9/Урок 1. Пример практического задания/task_1.py')
# >>> print(base_path)
# task_1.py
# >>>

# 6) Определение имени директории указанного пути 'path.dirname'
# >>> dir_path = os.path.dirname('/media/dk/Seagate Expansion Drive/Documents/GeekBrains/Python/Asynchron_chat/less9/Урок 1. Пример практического задания/task_1.py')
# >>> print(dir_path)
# /media/dk/Seagate Expansion Drive/Documents/GeekBrains/Python/Asynchron_chat/less9/Урок 1. Пример практического задания
# >>>

# 7) кортеж путь к родительской папке и название файла 'path.split'
dir_tuple = os.path.split('/media/dk/Seagate Expansion Drive/Documents/GeekBrains/Python/Asynchron_chat/less9/Урок 1. Пример практического задания/task_1.py')
# >>> dir_tuple = os.path.split('/media/dk/Seagate Expansion Drive/Documents/GeekBrains/Python/Asynchron_chat/less9/Урок 1. Пример практического задания/task_1.py')
# >>> print(dir_tuple)
# ('/media/dk/Seagate Expansion Drive/Documents/GeekBrains/Python/Asynchron_chat/less9/Урок 1. Пример практического задания', 'task_1.py')
# >>>




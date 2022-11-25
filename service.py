import os
from subprocess import Popen, CREATE_NEW_CONSOLE

# Создаем кортеж расширений файлов, которые будут нужны
EXT = ('.py', '.PY')
# Создаем список файлов с нужным расширением в текущей директории
files = [f.name for f in os.scandir() if f.is_file() and f.name.endswith(EXT)]
print('Файлы для упаковки:', files)
# Для Windows флаг CREATE_NEW_CONSOLE укажет создать новую консоль для процесса
packer = Popen(['7z', 'a', 'test.zip', *files],
               creationflags=CREATE_NEW_CONSOLE)
# Ждем завершения процесса, чтобы что-то делать дальше...
packer.wait()
print("Файлы упакованы, можно переименовывать")
# Переименовываем файл, созданный архиватором
os.rename('test.zip', 'backup.zip')

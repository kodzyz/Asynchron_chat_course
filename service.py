import subprocess

# p = subprocess.Popen(['mkdir', 'new folder'], shell=True, cwd='/home/username/projects')

# p = subprocess.Popen(['ls', '-l'], shell=True)
# python3 service.py
# common  logs  main.py  __pycache__  service.py  venv
# print(p, dir(p))

# subprocess.call('ls -l')
# subprocess.check_call()
# subprocess.run()

# Выполнить простую системную команду с помощью os.system()
ret = subprocess.call("ls -l", shell=True)
# Выполнить простую команду, игнорируя все, что она выводит
ret1 = subprocess.call("rm -f *.tmp", shell=True, stdout=open("/dev/null"))
# Выполнить системную команду, но сохранить ее вывод
p = subprocess.Popen("ls -l", shell=True, stdout=subprocess.PIPE)
out = p.stdout.read()
# Выполнить команду, передать ей входные данные и сохранить вывод
p = subprocess.Popen("wc", shell=True, stdin=subprocess.PIPE,
                     stdout=subprocess.PIPE, stderr=subprocess.PIPE)
s = b"Hello world!"
out1, err = p.communicate(s)  # Передать строку s дочернему процессу
# Создать два дочерних процесса и связать их каналом
p1 = subprocess.Popen("ls -l", shell=True, stdout=subprocess.PIPE)
p2 = subprocess.Popen("wc", shell=True, stdin=p1.stdout, stdout=subprocess.PIPE)
out2 = p2.stdout.read()

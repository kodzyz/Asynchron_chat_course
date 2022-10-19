from socket import *


def main():
    s = socket(AF_INET, SOCK_STREAM)
    s.connect(('localhost', 10000))
    tm = s.recv(1024)
    s.close()
    print("Текущее время: ", tm.decode('utf-8'))


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(e)

# (venv) dk@dk-ThinkPad-Edge-E540:~/PycharmProjects/Asynchron_chat/chat_lesson$ python3 client.py
# Текущее время:  Wed Oct 19 23:52:10 2022
#
# (venv) dk@dk-ThinkPad-Edge-E540:~/PycharmProjects/Asynchron_chat/chat_lesson$ python3 client.py
# Текущее время:  Wed Oct 19 23:52:13 2022
#
# (venv) dk@dk-ThinkPad-Edge-E540:~/PycharmProjects/Asynchron_chat/chat_lesson$ python3 client.py
# Текущее время:  Wed Oct 19 23:52:22 2022

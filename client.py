from socket import *


def main():
    s = socket(AF_INET, SOCK_DGRAM)
    s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

    while True:
        msg = 'Сообщение'.encode('utf-8')
        s.sendto(msg, ('localhost', 10000))


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(e)

# python3 client.py

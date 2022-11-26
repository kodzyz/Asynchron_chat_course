import ipaddress

# для операций с IP-адресами

# 1) создание адреса
# >>> import ipaddress
# >>> ipv4 = ipaddress.ip_address('192.168.0.1')
# >>> print(ipv4)
# 192.168.0.1

# 2) проверяется диапазон, к которому принадлежит адрес
# >>> print(ipv4.is_loopback)
# False
# >>> print(ipv4.is_multicast)
# False
# >>> print(ipv4.is_reserved)
# False
# >>> print(ipv4.is_private)
# True
# >>>
ip1 = ipaddress.ip_address('192.168.1.0')
ip2 = ipaddress.ip_address('192.168.1.255')
if ip2 > ip1:  # Сравнение ip-адресов
    print(True)  # True

print(str(ip1))  # 192.168.1.0 # Конвертация ip-адреса в строковое представление
print(int(ip1))  # 3232235776
print(ip1 + 5)  # 192.168.1.5
print(ip1 - 5)  # 192.168.0.251

# 3) Атрибут получения широковещательного адреса для сети — broadcast_address:
subnet = ipaddress.ip_network('80.0.1.0/28')
ba = subnet.broadcast_address
print(ba)  # 80.0.1.15

# 4) Просмотр всех хостов для объекта-сети — метод hosts():
print(list(subnet.hosts()))
# [IPv4Address('80.0.1.1'), IPv4Address('80.0.1.2'), IPv4Address('80.0.1.3'), IPv4Address('80.0.1.4'), IPv4Address('80.0.1.5'), IPv4Address('80.0.1.6'), IPv4Address('80.0.1.7'), IPv4Address('80.0.1.8'), IPv4Address('80.0.1.9'), IPv4Address('80.0.1.10'), IPv4Address('80.0.1.11'), IPv4Address('80.0.1.12'), IPv4Address('80.0.1.13'), IPv4Address('80.0.1.14')]

# 5) Разбиение сети на подсети (по умолчанию — на две) — метод subnets():
print(list(subnet.subnets()))  # [IPv4Network('80.0.1.0/29'), IPv4Network('80.0.1.8/29')]

# 6) Обращение к любому адресу в сети
print(subnet[1])  # 80.0.1.1 # Объект-сеть в Python представляется в виде списка ip-адресов,

# 7) создание объектов IPv4Interface или IPv6Interface
ipv4_int = ipaddress.ip_interface('10.0.1.1/24')
print(ipv4_int.ip)  # Получение адреса # 10.0.1.1
print(ipv4_int.netmask)  # Получение маски # 255.255.255.0
print(ipv4_int.network)  # Получение сети # 10.0.1.0/24

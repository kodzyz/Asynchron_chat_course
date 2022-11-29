# 0:37
class Shop:
    def __setattr__(self, cloth, price):  # key, value
        self.__dict__[cloth] = price  # [key] = value

    def __delattr__(self, item):
        self.__dict__.pop(item)


mos_shop = Shop()

# __setattr__
mos_shop.snikers = 1000
print(mos_shop.snikers)  # 1000
print(mos_shop.__dict__)  # {'snikers': 1000}

# __delattr__
del mos_shop.snikers
print(mos_shop.__dict__)  # {}

from abc import ABC, abstractmethod


class Shop(ABC):
    def __init__(self, name, price):
        self.name = name
        self.price = price

    @abstractmethod
    def clothing(self):
        raise NotImplementedError


# наследуемся и хотим добавить переменную(атрибут): super.__init__
class ShopRus(Shop):
    def __init__(self, name, price, margin):
        super.__init__(name, price)
        self.margin = margin

    def clothing(self):
        pass

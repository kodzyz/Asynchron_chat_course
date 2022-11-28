from abc import ABC, abstractmethod


class IPriceCar(ABC):
    def __init__(self, model, name, price, year):
        self.model = model
        self.name = name
        self.price = price
        self.year = year

    @abstractmethod
    def get_price(self):
        raise NotImplementedError  # если этот метод не вызван будет выводить ошибку


class KiaCar(IPriceCar):

    def info(self):
        return {'name': self.name, 'price': self.price, 'year': self.year, 'model': self.model}


car1 = KiaCar('ria', 'kia', 1000, 2022)
# Can't instantiate abstract class KiaCar with abstract methods get_price
# не реализован метод get_price


from abc import ABC, abstractmethod


class IPriceCar(ABC):
    def __init__(self, model, name, price, year):
        self.model = model
        self.name = name
        self.price = price
        self.year = year

    @abstractmethod
    def get_price(self):
        raise NotImplementedError  # если этот метод не вызван(у наследников) будет выводить ошибку


class KiaCar(IPriceCar):

    def info(self):
        return {'name': self.name, 'price': self.price, 'year': self.year, 'model': self.model}

    def get_price(self):
        pass


car1 = KiaCar('ria', 'kia', 1000, 2022)
print(car1.info())
# {'name': 'kia', 'price': 1000, 'year': 2022, 'model': 'ria'}

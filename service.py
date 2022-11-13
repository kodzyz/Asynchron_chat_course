def log_function(func):
    def wrapper(func):
        return func()
    return wrapper()

class RandomClass():

    @property
    def rated(self):
        return 3, 4

    @classmethod
    def make_number(cls):
        return 3

    @staticmethod
    def m():
        pass

    @log_function
    def our_func(self):


class User():

    def __int__(self) -> None:
        self.name = 'Andrey'

    def get_full_user_info(self):
        return self.name

    @staticmethod
    def get_all_users():
        pass
class LessMethod:

    def __init__(self, num_less, date_less, all_less):
        self.num_less = num_less
        self.date_less = date_less
        self.all_less = all_less

    @property
    def x(self):
        return self._num_less

    @x.setter
    def x(self, value):
        self._num_less = value + self.num_less

    @x.deleter
    def x(self):
        del self._num_less

    @x.getter
    def x(self):
        return self._num_less




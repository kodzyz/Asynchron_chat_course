# При использовании свойств (@property) доступ к атрибутам управляется серией пользовательских
# функций get, set и delete.
class C:
    def __init__(self):
        self._x = None

    @property  # свойство — вычисляемый атрибут (метод, обернутый декоратором @property);
    def x(self):
        """I'm the 'x' property."""
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    @x.deleter
    def x(self):
        del self._x


c = C()
# У свойств могут быть свои атрибуты — setter, getter, deleter:
setattr(c, 'x', 'value')
print(c.x)  # value
delattr(c, 'x')
print(c.x)  # AttributeError: 'C' object has no attribute '_x'


# То же самое может быть записано по-другому:
class C:
    def _get_x(self):
        """I'm the 'x' property."""
        return self._x

    def _set_x(self, value):
        self._x = value

    def _del_x(self):
        del self._x

    x = property(_get_x, _set_x, _del_x)

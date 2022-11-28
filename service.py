# Дескрипторы атрибутов

# листинг 2

# пример дескриптора, который контролирует тип значения для атрибута и препятствует
# удалению атрибута из экземпляра объекта

class TypedProperty:
    def __init__(self, name, type_name, default=None):
        self.name = "_" + name
        self.type = type_name
        self.default = default if default else type_name()

    def __get__(self, instance, cls):  # __get__(self, obj, type=None) — должен вернуть значение value;
        return getattr(instance, self.name, self.default)

    def __set__(self, instance, value):  # __set__(self, obj, value) — возвращает None
        if not isinstance(value, self.type):
            raise TypeError("Значение должно быть типа %s" % self.type)
        setattr(instance, self.name, value)

    def __delete__(self, instance):  # __delete__(self, obj) — возвращает None
        raise AttributeError("Невозможно удалить атрибут")


class Foo:
    name = TypedProperty("name", str)
    num = TypedProperty("num", int, 42)


f = Foo()
a = f.name  # Неявно вызовет Foo.name.__get__(f, Foo)
f.name = "Гвидо"  # Вызовет Foo.name.__set__(f, "Guido")
del f.name  # Вызовет Foo.name.__delete__(f)

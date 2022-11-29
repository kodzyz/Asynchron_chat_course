# GB = type('GB', (object,), {})
#
# Less = type(
#     'Less',
#     (GB,),
#     dict(attr=10)
# )
#
# gb = GB()
# print(gb.__class__)
# print(Less().attr)

# <class '__main__.GB'>
# 10

class GB(type):
    def __init__(self, *args, **kwargs):
        self.__in = None
        super().__init__(*args, **kwargs)

    def __call__(self, *args, **kwargs):
        if self.__in is None:
            self.__in = super().__call__(self, *args, **kwargs)
            return self.__in
        else:
            return self.__in


class Less(metaclass=GB):

    def __init__(self, name):
        self.name = name

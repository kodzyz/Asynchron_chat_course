class LessMethod:

    def __init__(self, num_less, date_less, all_less):
        self.num_less = num_less
        self.date_less = date_less
        self.all_less = all_less

    @classmethod
    def less(cls):
        return {
            'num_less': cls.num_less,
            'date_less': cls.date_less,
            'all_less': cls.all_less,
        }

    def real_less(self):
        self.num_less = 10
        self.date_less = 2022
        self.all_less = 16
        return self.all_less, self.date_less, self.num_less


class GBRealLess:
    data = 0

    def __init__(self):
        GBRealLess.data = GBRealLess.data + 90

    @classmethod
    def less(cls):
        print(GBRealLess.data)


gb_less = LessMethod(1, 2, 3)
gb_real_less1 = GBRealLess()
gb_real_less2 = GBRealLess()

print(gb_less.real_less())
print(gb_real_less2.less())

# (16, 2022, 10)
# 180
# None

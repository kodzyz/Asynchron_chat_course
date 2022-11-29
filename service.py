class LessMethod:

    def __init__(self, num_less, date_less, all_less):
        self.num_less = num_less
        self.date_less = date_less
        self.all_less = all_less

    @staticmethod
    def standart_lesson(theme):
        return {theme: f'{theme}'}

    def up_meta(self):
        return list(map(self.standart_lesson, self.all_less))


less1 = LessMethod(1, 2, [3, 4, 5])
print(less1.up_meta())  # [{3: '3'}, {4: '4'}, {5: '5'}]

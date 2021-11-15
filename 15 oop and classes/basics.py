class SomeClass:
    def __init__(self):
        self.some_attr = '123'

    def print_attr(self):
        print(f'this is attr = {self.some_attr}')

    def change_att(self, multiplier):
        print(self.some_attr * multiplier)


class1 = SomeClass()
print(class1.some_attr)
class1.print_attr()
class1.change_att(2)

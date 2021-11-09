class Parent:
    hair = 'black'

    def __init__(self):
        print('parent is createt')


class Child(Parent):
    hair = 'white'

    def __init__(self):
        super().__init__()
        print('child was created')


parent = Parent()
child = Child()
print()
print(parent.hair)
print(child.hair)


class Airplane:
    def fly_in_the_air(self):
        print('flying')


class Ship:
    def float_on_water(self):
        print('floating')


class FlyingBoat(Airplane, Ship):
    pass


sea_duck = FlyingBoat()
sea_duck.float_on_water()
sea_duck.fly_in_the_air()
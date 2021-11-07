# inheritance
"""
class Vehicle:
    def __init__(self):
        print('Vehicle created')

    def stat_ignition(self):
        pass

    def change_tire(self):
        pass


class Car(Vehicle):
    def __init__(self):
        print('Car created')


class Motorcycle(Vehicle):
    def __init__(self):
        print('Motorcycle created')


class LunarRover(Vehicle):
    def __init__(self):
        print('LunarRover created')


vehicle = Vehicle()
car = Car()
motor_cycle = Motorcycle()
lunar_rover = LunarRover()"""


# composition
class CombustionEngine:
    def __init__(self):
        print('Combustion engine created')


class Vehicle:
    def __init__(self):
        print('Vehicle created')

    def stat_ignition(self):
        pass

    def change_tire(self):
        pass


class Car(Vehicle):
    def __init__(self):
        print('Car created')


class Motorcycle(Vehicle):
    def __init__(self):
        print('Motorcycle created')


class LunarRover(Vehicle):
    def __init__(self):
        print('LunarRover created')


vehicle = Vehicle()
car = Car()
motor_cycle = Motorcycle()
lunar_rover = LunarRover()


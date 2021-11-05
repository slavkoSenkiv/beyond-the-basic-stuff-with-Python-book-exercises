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

class Mororcycle(Vehicle):
    def __init__(self):
        print('Mororcycle created')

class LunarRover(Vehicle):
    def __init__(self):
        print('LunarRover created')



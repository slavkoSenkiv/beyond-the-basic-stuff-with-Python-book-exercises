class PetrolEngine:
    def __init__(self):
        print('activate petrol engine')

    def change_power(self):
        print('changing petrol power')


class ElectricEngine:
    def __init__(self):
        print('activate electric engine')

    def change_power(self):
        print('changing electric power')


class Vehicle:
    def __init__(self):
        print('vehicle is created')
        self.engine = PetrolEngine()


class Car(Vehicle):
    def __init__(self):
        print('car is created')
        super().__init__()


class Tesla(Vehicle):
    def __init__(self):
        print('tesla is created')
        super().__init__()
        self.engine = ElectricEngine()


vehicle = Vehicle()
print()
car = Car()
print()
tesla = Tesla()
print()

vehicle.engine.change_power()
car.engine.change_power()
tesla.engine.change_power()




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

    """def change_spark_plug(self):
        print('spark plug was changed')"""


class ElectricEngine:
    def __init__(self):
        print('elecric engine created')


class Vehicle:
    def __init__(self):
        print('Vehicle created')
        self.engine = CombustionEngine()  # use this engine by default

    def stat_ignition(self):
        pass

    def change_tire(self):
        pass


class Car(Vehicle):
    def __init__(self):
        print('Car created')
        # super().__init__()


class Motorcycle(Vehicle):
    def __init__(self):
        print('Motorcycle created')
        super().__init__()


class LunarRover(Vehicle):
    change_spark_plug = None

    def __init__(self):
        print('LunarRover created')
        super().__init__()
        self.engine = ElectricEngine()  # use this engine instead of CombustionEngine


vehicle = Vehicle()
print()
car = Car()
print()
motor_cycle = Motorcycle()
print()
lunar_rover = LunarRover()
print()

"""vehicle.engine.change_spark_plug()
car.engine.change_spark_plug()
motor_cycle.engine.change_spark_plug()
lunar_rover.engine.change_spark_plug()"""

lunar_rover.change_spark_plug()
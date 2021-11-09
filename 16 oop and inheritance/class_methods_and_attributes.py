# <editor-fold desc="class methods demo">
class ExampleClass:
    def regular_method(self):
        print('this is regular method')

    @classmethod
    def class_method(cls):
        print('this is class method')


# call the class method w/o instantiating an object
# ExampleClass.class_method()
# ExampleClass().regular_method()
# print()
obj = ExampleClass()
# these lower lines are equivalent to the one above
# obj.class_method()
# obj.__class__.class_method()
# </editor-fold>

# <editor-fold desc="AsciiArt eg">
class AsciiArt:
    def __init__(self, characters):
        self._characters = characters

    @classmethod
    def fromFile(cls, filename):
        with open(filename) as fileObj:
            characters = fileObj.read()
            return cls(characters)

    def display(self):
        print(self._characters)


# Other AsciiArt methods would go here...
face1 = AsciiArt('________\n' +
                 '| .  . |\n' +
                 '| \\__/ |\n' +
                 '|______|')
# face1.display()
# face2 = AsciiArt.fromFile('face.txt')
# face2.display()
# </editor-fold>

# <editor-fold desc="class attributes demo">
class CreateCounter:
    count = 0

    def __init__(self):
        CreateCounter.count += 1


# print('Objects created:', CreateCounter.count)  # output = 0
a = CreateCounter()
b = CreateCounter()
c = CreateCounter()
# print('Objects created:', CreateCounter.count)  # output = 3
# </editor-fold>

# <editor-fold desc="static method demo">
class ClassWithStaticMethod:
    @staticmethod
    def say_hello():
        print('hello')

# Note that no object is created, the class name precedes sayHello():
ClassWithStaticMethod.say_hello()
# </editor-fold>

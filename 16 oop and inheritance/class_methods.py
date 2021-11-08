class ExampleClass:
    def regular_method(self):
        print('this is regular method')

    @classmethod
    def class_method(cls):
        print('this is class method')


# call the class method w/o instantiating an object
ExampleClass.class_method()
ExampleClass().regular_method()
print()
obj = ExampleClass()
# these lower lines are equivalent to the one above
obj.class_method()
obj.__class__.class_method()


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
face1.display()
face2 = AsciiArt.fromFile('face.txt')
face2.display()
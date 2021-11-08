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

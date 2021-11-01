class ParentClass:
    attr = 'abc'

    def parent_method(self):
        print('Hello world')


class ChildClass(ParentClass):
    """def parent_method(self):
        print('Hello world from child class')"""

    def child_method(self):
        print('ParentClass objects don"t have this method.')


class GrandChildClass(ChildClass):
    def grand_child_method(self):
        print('Only GrandchildClass objects have this method.')


print('\nCreate a ParentClass object and call its methods:')
parent = ParentClass()


print('\nCreate a ChildClass object and call its methods:')
child = ChildClass()


print('\nCreate a GrandchildClass object and call its methods:')
grand_child = GrandChildClass()




class ParentClass:
    attr = 'abc'

    def parent_method(self):
        print('Hello world')


class ChildClass(ParentClass):
    def parent_method(self):
        print('Hello world from child class')

    def child_method(self):
        print('ParentClass objects don"t have this method.')


class GrandChildClass(ChildClass):
    def grand_child_method(self):
        print('Only GrandchildClass objects have this method.')


print('\nParentClass:')
parent = ParentClass()
parent.parent_method()

print('\nChildClass:')
child = ChildClass()
child.parent_method()
child.child_method()

print('\nGrandchildClass:')
grand_child = GrandChildClass()
grand_child.parent_method()
grand_child.child_method()
grand_child.grand_child_method()





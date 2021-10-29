class ParentClass:
    attr = 'abc'

    def print_hello(self):
        print('Hello world')


class ChildClass(ParentClass):
    def some_new_method(self):
        print('ParentClass objects don"t have this method.')


class GrandChildClass(ChildClass):
    def another_new_method(self):
        print('Only GrandchildClass objects have this method.')


print('Create a ParentClass object and call its methods:')
parent = ParentClass()
parent.print_hello()
print()

print('Create a ChildClass object and call its methods:')
child = ChildClass()
child.print_hello()
child.some_new_method()
print()

print('Create a GrandchildClass object and call its methods:')
grand_child = GrandChildClass()
grand_child.print_hello()
grand_child.some_new_method()
grand_child.another_new_method()

print(ParentClass.attr)
print(ChildClass.attr)
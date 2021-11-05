# inheritance basics
# overwriting
# super method


class ParentClass:

    def parent_method(self):
        print('Hello world')

    def parent_method_for_super_eg(self):
        return '\n1. here is text for super eg in ParentClass'


class ChildClass(ParentClass):
    """here is an overwriting eg
    where method with the same name (parent_method) from ParentClass
    overwrites it's inheritance in ChildClass and farther in GrandChildClass
    and adjusts it. this change do not work on ParentClass."""
    def parent_method(self):
        print('Hello world from child class')

    def child_method(self):
        print('ParentClass objects don"t have this method.')

    def super_method_in_child_class(self):
        ChildClass_super_string = super().parent_method_for_super_eg() + '\n2. and this text has been added by super_method in ChildClass'
        return ChildClass_super_string


class GrandChildClass(ChildClass):

    def grand_child_method(self):
        print('Only GrandchildClass objects have this method.')

    def super_method_in_grand_child_class(self):
        GrandChildClass_super_string = super().super_method_in_child_class() + '\n3. and this text has been added by super_method in GrandChildClass'
        return GrandChildClass_super_string

    def super_method_in_grand_child_from_parent_class(self):
        GrandChildClass_string_with_super_from_ParentClass = super().parent_method_for_super_eg() + '\n2. and here we get method from ParentClass as super class '
        return GrandChildClass_string_with_super_from_ParentClass


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


print('\nplay with the super')
print('parent.parent_method_for_super_eg()', parent.parent_method_for_super_eg())
print('child.super_method_in_child_class()', child.super_method_in_child_class())
print('grand_child.super_method_in_grand_child_class()', grand_child.super_method_in_grand_child_class())
print('grand_child.super_method_in_grand_child_from_parent_class()', grand_child.super_method_in_grand_child_from_parent_class())





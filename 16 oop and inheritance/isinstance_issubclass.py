class ParentClass:
    pass


class ChildClass(ParentClass):
    pass


parent = ParentClass()
child = ChildClass()

print(isinstance(parent, ParentClass))
print(isinstance(parent, ChildClass))
print(isinstance(child, ChildClass))
print(isinstance(child, ParentClass))
print('_____')
print(isinstance(17, (str, float, bool, list, int)))
print('_____')
print(issubclass(ChildClass, ParentClass))
print(issubclass(ChildClass, str))
print(issubclass(ChildClass, ChildClass))
print(issubclass(ParentClass, ChildClass))


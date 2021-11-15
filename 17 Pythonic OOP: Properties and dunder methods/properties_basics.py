# <editor-fold desc="ClassWithRegularAttribute">
"""class ClassWithRegularAttribute:
    def __init__(self, some_parameter):
        self.some_attribute = some_parameter


obj = ClassWithRegularAttribute('some initial value')
print(obj.some_attribute)
obj.some_attribute = 'changed value'
print(obj.some_attribute)
print(dir(obj))
del obj.some_attribute
print(dir(obj))"""
# </editor-fold>


# <editor-fold desc="ClassWithProperties">
"""class ClassWithProperties:
    def __init__(self):
        self._some_attribute = 'some initial value'

    @property
    def some_attribute(self):
        return self._some_attribute

    @some_attribute.setter
    def some_attribute(self, value):
        self._some_attribute = value

    @some_attribute.deleter
    def some_attribute(self):
        del self._some_attribute


obj = ClassWithProperties()
print(obj.some_attribute)
obj.some_attribute = 'changed value'
print(obj.some_attribute)
print(dir(obj))
del obj.some_attribute
print(dir(obj))"""
# </editor-fold>


class ClassWithBadProperty:
    def __init__(self):
        self._some_attribute = 'some initial value'

    @property
    def some_attribute(self):
        # We forgot the _ underscore in `self._someAttribute here`, causing
        # us to use the property and call the getter method again:
        return self.some_attribute

    @some_attribute.setter
    def some_attribute(self, value):
        self._some_attribute = value


obj = ClassWithBadProperty()
print(obj.some_attribute)
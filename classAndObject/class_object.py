class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f'name={self.name} age={self.age}'


s1 = Student(name="test", age=20)
l1 = [1, 2, 3]
d1 = {1: 1, 2: 2}
# Student.__bases__
'''
<type 'type'>
type of all types
<type 'upject'>
base of all other types

'''

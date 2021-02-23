s1 = ('Richard',20)
s2 = ('Chris', 21)
print(s1[0], s1[1])

class Student:
  def __init__(self, name, age):
    self.name = name
    self.age = age

s1 = Student('Jack', 26)
s2 = Student('Tim', 20)
print(s1.name)
print(s2.age)

from collections import namedtuple
Students = namedtuple('Students', ['name', 'age'])
s3 = Students("Paul", 55)
s4 = Students('Nico', 49)
print(s3.name)
print(s4.age)
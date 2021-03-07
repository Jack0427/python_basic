# class People:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def __eq__(self, other):
#         return (other.name, other.age) == (self.name, self.age)


# p1 = People('A', 20)
# p2 = People('A', 20)


from dataclasses import dataclass


@dataclass
class NewPeople:
    name: str
    age: int


p1 = NewPeople('A', 20)
p2 = NewPeople('A', 20)

print(p1, p2)
print(f"{p1 == p2= }")

import pickle

import people
# class People:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def sayhi(self):
#         print(f'Hi my name is {self.name} and I\'m {self.age}')


f = open('p1', 'rb')
p2 = pickle.load(f)
f.close()
p2.sayhi()

class People:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sayhi(self):
        print(f'Hi my name is {self.name} and I\'m {self.age}')


'''
二進制文件 看成字串 若是用引入的方式寫成二進制文件 讀取的時候就要用同樣的方式
ex p1 = People('jack',26)
讀取的時候
不能是

import people

p2 = people.People

'''

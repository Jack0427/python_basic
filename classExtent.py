# subclass extend supclass everthing
# 子類的方法只有子類能使用
# 子類有同樣的方法即改寫稱為多態
# type 判斷是甚麼類 isinstance判斷是不是那個類(Boolean)
class Animal:
    count = 0  # 類的屬性 不須有實例 就能訪問

    def __init__(self, leg):
        self.leg = leg  # 實例的屬性 有實例才能訪問

    def eat(self):
        print("Animal is eating")


class Bird(Animal):
    def __init__(self, leg, nose):
        super().__init__(leg)
        self.nose = nose

    def sing(self):
        print('Bird is singing')

    def eat(self):
        print("Bird is eating")

    def getAttribute(self):
        print(f'leg = {self.leg}, nose = {self.nose}')


# class Dog(Animal):
#     def eat(self):
#         print("Dog is eating")


class Duck(Bird):
    def __init__(self, leg, nose, color):
        super().__init__(leg, nose)
        self.color = color

    def getAttribute(self):
        print(f'leg = {self.leg}, nose = {self.nose}, color = {self.color}')

# duck = Duck()

# b = Bird()
# # b.eat()
# d = Dog()
# # d.eat()


# print(type(b))
# print(isinstance(b, Bird))
# print(isinstance(duck, Bird))
testBird = Duck(2, 1, 'red')
testBird.getAttribute()

# self實例本身 cls本身
# classmethiod 類方法
# staticmethiod 靜態方法
# 先後順序 staticmethiod -> classmethiod -> 實例方法
class Student:
    count = 0  # 不須實例可訪問

    def __init__(self, name):
        Student.count += 1
        self.name = name  # 有實例才可訪問

    def sayhi(self):  # 實例話才可被調用
        print(__name__)
        if __name__ == '__main__':
            print('hi~')
        print(f'Hi my name is {self.name}')

    @classmethod
    def test(cls):
        print(cls.count)

    @staticmethod
    def test1():  # 完全獨立的方法 不能調用類裡面的其他方法
        print("it's a staticmethiod")

    # def test2(): 如果未給裝飾器 需傳入self 否則實例化調用會出錯
    #     print("it's a normal function")


# print(Student.count)
# s1 = Student(name='Alice')
# print(s1.name)
# print(s1.count)
# s1.count = 1
# print(s1.count)
# print(Student.count)
# Student.count = 2 可直接修改 之後產生的實例 count為2
# print(Student.count)
# s2 = Student(name="Tomy")
# print(Student.count)
# s1 = Student('a')

# Student.test()
s1 = Student('classatr')
s1.sayhi()
# s1.test()
# Student.test()
# s1.test1()
# Student.test1()

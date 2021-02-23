# 前綴為class
# attribut and methiod
# methiod's first pramater si self(js's this)
# self __init__ 內設置屬性 _代表受保護的 可以更改也可以從外面獨拿到該屬性
# __代表私有的 實例拿不到 只能在該class中修改與獲取
# 通常都使用_protect_ __private_做前綴
# 透過dir 可以拿到該實例能拿到的所有屬性 __為開頭的屬性 需要加_類的名稱 即可訪問修改

class People:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self._protect_var = 10  # 被保護的
        self._var = 10  # 被保護的
        self.__private_var = 10  # 只能在class中使用
        self.__ll = 10  # 只能在class中使用

    @property  # 訪問私有屬性 可以做判斷
    def ll(self):
        return self.__ll

    @ll.setter  # 設置私有屬性 可以做判斷
    def ll(self, val):
        if val < 10:
            print('too low')
        else:
            self.__ll = val

    def sayHi(self):
        print(f'Hi! my name is {self.name} and I am {self.age}')

    def getll(self):
        print(self.__ll)

    def setll(self, val):
        self.__ll = val


jack = People('Jack', 26)
# jack.age = 30  # 可直接修改
# print(dir(jack))
# jack._People__ll = 20
# jack.getll()
jack.ll = 20
print(jack.ll)

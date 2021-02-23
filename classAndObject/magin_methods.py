'''
double underscore
雙下滑線開頭跟結尾的
又稱dunder
可以直接使用python原本的方法 例如len
'''


class Account:
    def __init__(self, name, amount=0):
        self.name = name
        self.amount = amount
        self._transaction = []

    @property  # 作為屬性訪問
    def balance(self):
        return self.amount + sum(self._transaction)

    def __len__(self):
        return len(self._transaction)
    # print默認調用這個方法 若沒有則調用 __repr__

    def __repr__(self):  # 建議使用
        return f'Account({self.name} {self.amount})'

    # def __str__(self):
    #     return f'name={self.name} amount={self.amount}'
    def add_transaction(self, amount):
        self._transaction.append(amount)

    def __eq__(self, other):  # ==
        return self.balance == other.balance

    def __lt__(self, other):  # <
        return self.balance < other.balance


a = Account('Jack', 10)
# print(len(a))
# print(repr(a))
# print(str(a))
# print(a)
a.add_transaction(100)
a.add_transaction(-20)
print(a.balance)
b = Account('test', 50)
b.add_transaction(70)
b.add_transaction(-20)
print(b.balance)
print(a == b)
print(a < b)

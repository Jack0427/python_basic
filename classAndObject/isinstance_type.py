
'''
isinstance(x,y) x是否為y的子類
type(x) 誰實例化x
'''


class A:
    pass


class B(A):
    pass


class C:
    pass


a = A()
b = B()
# isinstance(b,B) or isinstance(b,A) or isinstance(b,C)
print(isinstance(b, (B, A, C)))

# 匿名函數

def test(x, y):
    return x + y


def lambdatest(a, b, f):
    return f(a, b)


# print(lambdatest(1, 2, lambda a, b, : a*2+b*2))

def add_m(a):
    return lambda n: a + n


add10 = add_m(10)

print(add10(20))

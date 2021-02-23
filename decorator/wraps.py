import functools


def demo(f):
    # def f_new(x):
    #     print(f.__name__)
    #     return f(x)
    @functools.wraps(f)
    def f_new(*args, **kwargs):
        print(f.__name__)
        return f(*args, **kwargs)  # 不限參數 跟關鍵字參數
    # f_new.__name__ = f.__name__
    # f_new.__doc__ = f.__doc__
    return f_new


@demo
def fn1(x):
    """
    hello this is a fn1
    """
    return x * 2 * x


print(fn1.__name__)  # 會被修改成demo retun 的 f_new
print(fn1.__doc__)

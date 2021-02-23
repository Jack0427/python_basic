# 若要使用裝飾器 要注意參數問題
# 裝飾器意義
#
# @demo
# def fn1(x):                             -> demo(fn1)
#     return x * 2 * x
#
#
#
def demo(f):
    # def f_new(x):
    #     print(f.__name__)
    #     return f(x)
    def f_new(*args, **kwargs):
        print(f.__name__)
        return f(*args, **kwargs)  # 不限參數 跟關鍵字參數
    return f_new


@demo
def fn1(x):
    return x * 2 * x


@demo
def fn2(x, y):
    print('hello')


def demo_new(s):
    def demo(f):
        # def f_new(x):
        #     print(f.__name__)
        #     return f(x)

        print(s)

        def f_new(*args, **kwargs):
            print(f.__name__)
            return f(*args, **kwargs)  # 不限參數 跟關鍵字參數
        return f_new
    return demo


@demo_new('heelp')
def fn3(x, y):
    print(f'x={x} y={y}')


# demo_new('heelp')(fn3)
# demo(fn3)
# f_new()
fn3(5, 6)

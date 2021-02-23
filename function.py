def test(a, b):
    print(a, b)
    return a + b


# print(test(5, 6))  # 位置參數
# print(test(a=6, b=8))  # 關鍵字參數


def my_max(list):
    if not list:
        return None
    max_val = list[0]
    for it in list:
        if it > max_val:
            max_val = it
    return max_val


# print(my_max([5, 8, 9, 5, 2, 0, 1, 2, 3, 11]))

# not None == not False == not '' == not 0 == not [] == not {} == not () 空的 none 都是false


def append(a):
    # a = a + [12]  # [5,6,12]
    a.append([12])
    print(a)


a = [5, 6]
# append(a)  # [5,6,12]  [5,6], [5,6,12] [5,6,12]
# 若方法裡面有 = 會重新宣告一個變數 若沒有會修改外面傳進來的參數(複雜類型才會)
# 若要修改簡單類型使用global

z = 1


def demo(a):
    global z
    z = z + a
    print(z)


# demo(5)

# 可變參數


def addarg(*args):
    print(args)
# 參數前加* 不限傳入參數個數 args為一個tuple


def addkwargs(**kwargs):
    print(kwargs)
# 參數前加** 不限傳入參數個數 kwargs為一個dict


def testwarg(a, b, c):
    print(a, b, c)


def wargtest(z, **kwargs):
    if z == 2:
        z = {**kwargs}
        print(z)
        testwarg(**kwargs)


wargtest(2, a=1, b=2, c=3)

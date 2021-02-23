import pdb
# pdb.set_trace()
"""
進入pdb 命令行書入 ? 查找命令
s step 遇到函數會進到函數內
n next 遇到函數不會進到函數內 直接返回執行後的結果
l list 附近代碼顯示
p 顯示該變量 已執行的
"""
list_a = [5, 6, 8, 10, 22, -4, -9, 5]
list_even = []


def filter_envet(list_val):
    for it in list_a:
        if it % 2 == 0:
            list_even.extend(it)


filter_envet(list_a)

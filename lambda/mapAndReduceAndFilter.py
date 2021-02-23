# list_a = [1, 2, 3, 4]
# list_a2 = [item for item in map(lambda x: x ** 3, list_a)]

# dict_a = {'name': 'Ben', 'name2': 'Hel'}
# dict_a2 = {key+'s': val+'lo' for key, val in dict_a.items()}

# map用於可迭代物件 多配合於解析 第一個參數為fun 用作處理每個迭代內容 第二個為迭代物件

# from functools import reduce
# list_a = [1, 2, 3, 4]
# set_a = {1, 2, 3, 4, 5}
# print(reduce(lambda x, y: x*2+y*2, set_a))
# reduce 用於可迭代物件 多配合於解析 第一個參數為fun內有兩個參數 用作處理第一個迭代內容及第二個迭代內容 第二個為迭代物件 返回所有迭代內容之合

# filter_a = [1, 2, 3, 4]
# filter_a2 = [item for item in filter(lambda x:x % 2 == 1, filter_a)]
# filter_a3 = [item for item in filter_a if item % 2 == 1]
# a2 a3 相同 若數據龐大的話 會使用a2

data = [
    {'name': 'a1', "age": 20},
    {'name': 'a2', "age": 25},
    {'name': 'a3', "age": 26},
    {'name': 'a4', "age": 29},
    {'name': 'a5', "age": 24},
    {'name': 'a6', "age": 21},
    {'name': 'a7', "age": 26},
    {'name': 'a8', "age": 28},
    {'name': 'a9', "age": 22},
    {'name': 'a10', "age": 24},
    {'name': 'a11', "age": 26},
    {'name': 'a12', "age": 25},
    {'name': 'a13', "age": 27},
]
# 取出裡面age > 25的
print([it for it in data if it.get('age') > 25])

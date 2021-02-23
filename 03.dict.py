'''
字典用{}表示
key為不可改變的類型 int str tuple
可以直接新增或修改
dict['a'] = 56
dict.update(dict1) dict1內容加到dict中
{**dict,**dict1} 解構
'''
dict1 = {
    'a': 213,
    (5, 60): 'abc'
}
x = ('b', 'c')
dict2 = dict(a=5, b=6, x='abc')
z = 'a'
# print(dict1.get('z'))
'''
訪問的方式
dict[key] ->若key沒有值 程序會報錯
dict.get(key) -> 若key沒有值 程序不會報錯 返回none
'''
'''
len(d)                            字典有幾對元素
str(d)                            用字串方式列出整個字典
d.keys()                          字典所有key 返回迭代器 需用list tuple...轉
d.values()                        字典所有val 返回迭代器 需用list tuple...轉
d.items()                         返回hash 類型tuple
d.pop(key)                        移除字典key為key 並返回
d.popitem()                       移除字典最後一個 並返回
del d[key]                        移除字典key
del d                             清除字典
d.clear()                         清空字典
d.update(dict)                    dict加入d中
d.copy()                          淺複製
d.fromkeys(seq[,val])             產生新字典 seq會被迭代成每一個name val會成為每一個val
d.get(key, default=None)          返回d[key] 若沒有返回default
d.setdefault(key, default=None)   與get相似 若沒有key 新增值設為default
key in d                          d是否有key
'''

arr = ['a', 'b', 'c']
arr1 = ['a1', 'b1', 'c1']
dict1 = dict1.fromkeys(arr, arr1)
# print(dict1) # {'a': ['a1', 'b1', 'c1'], 'b': ['a1', 'b1', 'c1'], 'c': ['a1', 'b1', 'c1']}
dict2 = {
    'a': 1,
    'b': 2
}
print(dict2.get('c', 5))
print(list(dict2.keys()))

'''
set大括號建立
無序
不重複的
'''
s = {'a', 'b'}
s.discard
str1 = '2132154'
a = list(set(str1))
a.sort() # 只做排列不回傳
s.clear()
# print(a)
# print(s) # set()
'''
len(s)              s有多少元素
s.add(x)            新增x
s.remove(x)         移除x 若沒有會報錯
s.discard(x)        移除X 不會報錯
s.pop()             隨機刪除(因set無序排列，刪除最左邊的)
s.clear()           清空s
x in s              s是否有x
s.copy()            複製

s & s1              交集 兩個都有的
s | s1              並集 兩個相加去重
s ^ s1              對稱差集 兩個相加去重去交集
s - s1              差集 s有 s1沒有的

https://www.lfhacks.com/tech/python-set-operations
https://www.runoob.com/python3/python3-set.html
'''

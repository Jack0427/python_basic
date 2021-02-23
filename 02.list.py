import important
'''
切片方式
[start:end:step]
結果不包含end 只到end前面一位
[:] 包含全部內容 拷貝的意思
[:3] = [0:3]
[0:5:3] 取index = 0 and index = 3的值
反向取值
a = [1, 2, 3, 4, 5, 6]
d = a[5:0:-1] # [6, 5, 4, 3, 2]
c = a[::-1] # [6, 5, 4, 3, 2, 1]
'''
# 獲取列表機本信息
list1 = [1, 2, 3, 5, 8, 5, 3, 2, 46, -10]
# print(f'list1的長度為{len(list1)}')
# print(f'list1的最大值為{max(list1)}')
# print(f'list1的最小值為{min(list1)}')
# print(f'list1的出現3的次數為{list1.count(3)}')
list2 = ['a', 'c', 'd']
# 加入一個元素
list2.append('e')
# 特定位置插入
list2.insert(1, 'b')
# 刪除元素
list2.remove('c')
# 列表翻轉
list2.reverse()
# 列表排序
list1.sort()  # 預設為小到大
list1.sort(reverse=True)  # reverse後 大到小

# 若有比較的方法 列表內的元素要統一
listtest = [1, 2, 'abc', [58, 67], 1]

'''
列表函數
len(list) 求長度
max(list) 求最大值
min(list) 求最小值
list(seq) 將元組轉換為列表

列表方法
list.append(obj) 添加在最後
list.count(obj) obj在列表出現幾次
list.extend(seq) 新增一個序列裡面的內容在最後
list.index(obj) obj的位置
list.insert(index,obj)在index插入obj
list.pop([index = -1])默認最後一個值 返回被刪除的值
list.remove(obj)移除列表中的obj
list.reverse()反轉列表不回傳
list.sort(key=None,reverse=False)排序 默認小到大
list.clear()清空列表
list.copy()複製列表
'''
# 冒泡排序


def buboo(arr):
    totalLen = len(arr)
    for i in range(totalLen):
        for j in range(totalLen - i - 1):  # -1是因為最後一位是長度-1 -i是因為有跑過的且最大的已經在最後一位了 不需要再跑了
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


arr = [5, -1, 2, 3, 4, 6, 9, 2, 0]
buboo(arr)
print(arr)
'''
tuple and list 
元組不可改變，創建時只需一個內存
列表可改變，創建時須兩塊，一塊是固定的一塊是提供擴展的，較靈活
'''

a = 2
b = 0b1010  # 2進制
c = 0o12  # 8進制
d = 0xa  # 16進制

'''
整數除法 / 精確計算 type float  // type int
float做運算 結果都是float
'''
# print(type(4 / 2))  # float
# print(type(3//2))  # int

name = 'python'
age = 27
new_str = 'I am %s today %d' % (name, age)  # python2
new_str_1 = 'I am {} today {}'.format(name, age)  # python3 不會有數據類型的問題
new_str_2 = 'I am {name} today {age}'.format(
    name=name, age=age
)
new_str_3 = f'I am {name} today {age}'  # python3.6
# print(new_str)
# print(new_str_1)
# print(new_str_2)
# print(new_str_3)


'''
string -> list
str.split() 填入要做為區分的字元 預設為空白
list -> string
" ".join(list) join前面放入要將內容串起來的文字
'''
str_list = 'google.com.apple'
# print(str_list.split('.'))  #['google', 'com', 'apple']
list_str = ['google', 'com', 'apple']
# print('~'.join(list_str))  #google~com~apple

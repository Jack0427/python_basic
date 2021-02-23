import sys
# sep = 分割符號 end =結尾符號 file = 輸出文件
print('hello', 'world', sep='~', end='!', file='sys.stdout')
# windows中 按ctrl + 方法 可看到方法的介紹
sys.stdout.write('hello~world!')

a = input('dddddd:')
print(a, type(a))
b = sys.stdin.readline()  # 輸入 按enter不會停止 要輸入 ctrl+d ctrl+z
print(b, type(b))  # class 'list'

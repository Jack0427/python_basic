import os
from pathlib import Path, WindowsPath

# 由路徑去操作檔案

f_route = os.path.join(os.getcwd(), 'demo', 'test.txt')

# print(f_route)
# print(Path.cwd()) # 當前目錄

a = Path.cwd()
# a.glob("*") 所有路徑下的文件
# a.rglob("*") 所有路徑下的文件包含資料夾內的資料 可加過濾的文件 *為所有


for file in a.rglob("*.txt"):
    print(file)
# print(a)
# apple = a / 'apple'
# if not apple.is_dir():
#     apple.mkdir()  # 先有路徑才可以mkdir()
# # f_apple = open(apple / 'test.txt', 'w')
# elif apple.is_dir():
#     if os.listdir(apple):
#         print('no')
#     else:
#         print('yes')
#         apple.rmdir()  # 有東西不能刪
# apple.rmdir()
# b = (a / 'demo' / 'test.txt')
# f = open(b, 'w') #開新檔案
# f.write('hello \n')
# f.write('hello \n')
# f.close()
# print(b.is_file())

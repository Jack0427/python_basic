from pathlib import Path

a = Path.cwd()

# f = open(a / 'test.txt', 'wb')  # w不能寫入二進制文件 使用wb
# f.write(b'its a very good day')
# f.close()


fe = open('test1.txt', 'rb')
for line in fe:
    print(line)
fe.close()

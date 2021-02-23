from collections import deque
import time
# list查找 大數據 速度較快
# deque插入 異動數據 大數據 速度較快

d = deque(range(10000000))
l = list(range(10000000))

t1 = time.time()
# d.append(-1)
print(d[59999])
# d.insert(11210, -1)
print(f'deque:{time.time()-t1}')

t2 = time.time()
# l.append(-1)
print(l[59999])
# l.insert(11210, -1)
print(f'list:{time.time()-t2}')

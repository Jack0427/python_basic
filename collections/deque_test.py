from collections import deque
# 左右兩邊都可操作
d = deque([1, 2, 3])
d.append(4)
print(d)
d.appendleft(0)
print(d)

d.pop()
print(d)
d.popleft()
print(d)

d.extend([4, 5])
print(d)
d.extendleft([0, -1])
print(d)

d.reverse()
print(d)

d.insert(0, 123)
print(d)

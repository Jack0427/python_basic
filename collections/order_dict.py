from collections import OrderedDict

# d = dict()
# d['c'] = 3
# d['a'] = 1
# d['b'] = 2
d = OrderedDict()
d['c'] = 3
d['a'] = 1
d['b'] = 2
print(d)
d.move_to_end('c')
print(d)

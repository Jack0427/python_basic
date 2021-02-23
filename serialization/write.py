import pickle

import people


p1 = people.People(name='Jack', age=26)

f = open('p1', 'wb')
pickle.dump(p1, f)
f.close()

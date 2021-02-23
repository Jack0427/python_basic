a = [1, 2, 3, 4, 5]
b = [item * 2 for item in a]  # [2,4,6,8,10]
c = [item for item in a if item % 2 == 0]  # [2,4]

person = {"name": 'jack', "age": 26}
dic_p = {key: val for key, val in person.items() if val == 26}
set_p = {key for key in person.keys()}
print(set_p)

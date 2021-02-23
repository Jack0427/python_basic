from collections import defaultdict
word_list = ['is', 'who', 'when', 'it', 'is', 'who', 'is']
result = dict()
# for word in word_list:
#     if word not in result:
#         result[word] = 1
#     else:
#         result[word] += 1

# print(result)

# for word in word_list:
#     result.setdefault(word, 0)
#     result[word] += 1

# print(result)

result = defaultdict(int)  # 若沒有先給默認 給可調用的值
for word in word_list:
    result[word] += 1
# print(result)


res = defaultdict(lambda: {'name': '', 'age': 0})
res[0]['name'] = 'Aicea'
print(res[0])

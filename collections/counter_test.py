from collections import Counter

word_list = ['is', 'who', 'is', 'it', 'it', 'it', 'who',
             'it', 'is', 'whoit', 'it',  'who', 'is', 'is', ]
c = Counter(word_list)
# print(c)

d = Counter('aassdddddasdsdhapvnaodsijfosdf')
# print(d.most_common(3))  # top n
d.update('cccccccccccccccccccccccc')  # 在第一次基礎上 繼續做計算
print(d)

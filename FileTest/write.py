# x 創立新文件，並寫入 若已經有文件了 會噴錯
# w 沒有的話創建 有的話覆蓋文件內容
# a 新增內容
# 若要中文要使用 encoding="utf-8"

f = open('text.txt', mode='w', encoding="utf-8")
f.write('hello~~!!!!~\n')
f.writelines([
    'x 創立新文件，並寫入 若已經有文件了 會噴錯\n',
    'w 沒有的話創建 有的話覆蓋文件內容\n',
    'a 新增內容"\n',
    '若要中文要使用 encoding="utf-8"'])
f.close()

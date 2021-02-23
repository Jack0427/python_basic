# 文件一定要存在 中文的話要使用utf-8
f = open('text.txt', encoding="utf-8")
# a = f.read() 效率差
# b = f.readline() 一次只讀取一行 下次執行會讀取下一行 會標記指針 使用f.close() f.seek(0) 可以清除指針 在運行會從第一行開始
# c = f.readlines() 回傳list 若文件很大內存會爆炸
# for line in f:
#     print(line, end='.')
# for line in f:
#     print(line, end='.')  # 文件打開後就會標記指針 指針已經到最後就不會再次讀取了
# f.close()

with open('text.txt', encoding="utf-8") as f:  # 使用with 就不需使用close
    for line in f:
        print(line)

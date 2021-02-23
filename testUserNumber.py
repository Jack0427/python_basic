import important
import random
# b = int(input('請設定一個數字:'))
c = random.randint(0, 100)
while True:
    a = int(input('猜一個0-100間的數字:'))
    if a > c:
        print('太大囉~')
    elif a < c:
        print('太小囉~')
    else:
        print(f'恭喜答案就是{c}!')
        break

print('感謝參與!')

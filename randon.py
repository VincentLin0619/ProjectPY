import random

numstart = input('請定義初始數： ')
numend = input('請定義結束數： ')
numstart = int(numstart)
numend = int(numend)

x = random.randint(numstart, numstart)
count = 0

while True:
    count += 1
    ans = input('請輸入你猜的數字： ')
    ans = int(ans)

    if ans == x:
        print('你猜對了！')
        print('你總共猜了', count, '次')
        break
    elif ans < x:
        print('猜的小於答案')
    elif ans > x:
        print('猜的大於答案')

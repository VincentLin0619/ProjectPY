def check_year(y):
    # four = y % 4
    # fourth = y % 400
    if (y % 4) == 0 or (y % 400) == 0:
        return '閏年'
    else:
        return '平年'


x = input('請輸入年份：')
x = int(x)
print(x, '年為', check_year(x))

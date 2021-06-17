# 確認有無檔案
import os  # operating system
products = []
if os.path.isfile('product.csv'):
    print('找到檔案')
# 讀取檔案
    with open('product.csv', 'r', encoding='utf-8') as f:
        for line in f:
            if '商品,價格' in line:
                continue  # 跳過並繼續
            name, price = line.strip().split(',')
            products.append([name, price])
else:
    print('找不到檔案...')
    exit()
# 使用者輸入
while True:
    name = input('請輸入商品：')
    if name == 'q':
        break
    price = input('請輸入價格：')
    name = str(name)
    price = int(price)
    products.append([name, price])

# 寫入檔案
with open('product.csv', 'w', encoding='utf-8') as f:
    f.write('商品,價格\n')
    for product in products:
        f.write(product[0] + ',' + str(product[1]) + '\n')

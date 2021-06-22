import os  # operating system

# 讀取檔案


def read_file(filename):
    products = []
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            if '商品,價格' in line:
                continue  # 跳過並繼續
            name, price = line.strip().split(',')
            products.append([name, price])
    return products

# 使用者輸入


def user_input(products):
    while True:
        name = input('請輸入商品：')
        if name == 'q':
            break
        price = input('請輸入價格：')
        name = str(name)
        price = int(price)
        products.append([name, price])
    return products


# 寫入檔案
def write_in_file(filename, products):
    with open(filename, 'w', encoding='utf-8') as f:
        f.write('商品,價格\n')
        for product in products:
            f.write(product[0] + ',' + str(product[1]) + '\n')


# 先檢查檔案在不在
def main():
    filename = 'product.csv'
    if os.path.isfile(filename):
        print('找到檔案')
        products = read_file(filename)
    else:
        print('找不到檔案...')
        exit()
    products = user_input(products)
    write_in_file('product.csv', products)


main()

products = []

while True:
    name = input('請輸入商品：')
    if name == 'q':
        break
    price = input('請輸入價格：')
    products.append([name, price])
with open('product.csv', 'w') as f:
    for product in products:
        f.write(product[0] + ',' + product[1] + '\n')

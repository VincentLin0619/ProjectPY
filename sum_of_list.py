data = []

while True:
    new_list = input('請增加列表：')
    new_list = str(new_list)
    if new_list == 'q':
        break
    data.append(int(new_list))

print(sum(data))

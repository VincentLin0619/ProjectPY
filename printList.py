data = [1, 2, 3, 4, 5, 6, 7]

with open('printList.txt', 'w') as f:
    for p in data:
        p = str(p)
        f.write(p + '\n')

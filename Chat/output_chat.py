
# 讀取檔案
def readfile(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        data = []
        for line in f:
            data.append(line.strip())
        f.close()
    return data

# 判斷人名並轉換格式


def convert(data):
    new = []
    name = None
    for l in data:
        if l == 'Allen':
            name = 'Allen'
            continue
        elif l == 'Tom':
            name = 'Tom'
            continue
        if name:
            new.append(name + ': ' + l)
    return(new)

# 寫入檔案


def write_file(filename, data):
    with open(filename, 'w', encoding='utf-8') as f:
        for new in data:
            f.write(new + '\n')


def main():
    data = readfile('input.txt')
    data = convert(data)
    write_file('output.txt', data)


main()

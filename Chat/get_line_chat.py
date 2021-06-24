def readfile(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        data = []
        for line in f:
            data.append(line.split())
        f.close()
    return data


def main():
    data = readfile('[LINE]曹.txt')
    print(data)
    # data = convert(data)
    # write_file('[LINE]曹.txt', data)


main()

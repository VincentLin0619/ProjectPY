
data = []

with open('test.txt', 'r') as f:  # 打開檔案 並且當作 f
    for line in f:
        data.append(line.strip())  # 刪除換行符號 '\n'
print(data)

password = 'a1234'
j = 3
while True:
    userpassword = input('請輸入你的密碼： ')
    if userpassword == password:
        print('登入成功！！！')
        break
    elif j > 0:
        print('你還剩餘', j, '次機會登入')
        j = j - 1
    else:
        print('你沒機會了！滾')
        break

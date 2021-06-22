

def add_data():
    data = []
    while True:
        user_send = input('請增加表單')
        user_send = str(user_send)
        if user_send == 'q':
            data.append(user_send)
            break
    return data


print(add_data())


# def sum_of_list():
#     return sum()

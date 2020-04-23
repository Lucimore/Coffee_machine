my_list = []
while True:
    number = input()
    if number == '.':
        break
    my_list.append(float(number))
print(min(my_list))
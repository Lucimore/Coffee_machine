my_list = []
while True:
    x = input()
    if x == '.':
        break
    my_list.append(int(x))
total = 0
for n in my_list:
    total += n
print(total / len(my_list))

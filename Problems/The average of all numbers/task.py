# put your python code here
my_list = []
for x in range(int(input()), (int(input()) + 1)):
    if int(x) % 3 == 0:
        my_list.append(x)
total = 0
count = 0
for _ in my_list:
    total += my_list[count]
    count += 1
print(total / count)

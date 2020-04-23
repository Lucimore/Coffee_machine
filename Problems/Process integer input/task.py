# put your python code here
my_list = []
while True:
    number = int(input())
    if number < 10:
        continue
    if number > 100:
        break
    my_list.append(number)
for n in my_list:
    print(n)

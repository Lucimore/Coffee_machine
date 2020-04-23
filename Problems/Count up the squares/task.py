# put your python code here
my_list = []
while True:
    number = int(input())
    my_list.append(number)
    if my_list[0] == 0:
        break
    total = 0
    for n in my_list:
        total += n
        if total == 0:
            break
    if total == 0:
        break
answer = 0
for n in my_list:
    answer += n * n
print(answer)
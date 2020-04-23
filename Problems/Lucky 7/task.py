number = int(input())
mylist = []
for _ in range(number):
    mylist.append(int(input()))
for n in mylist:
    if int(n) % 7 == 0:
        print(int(n) ** 2)

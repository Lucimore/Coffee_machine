scores = input().split()
# put your python code here
win, lose = 0, 0
for n in scores:
    if n == 'C':
        win += 1
    if n == 'I':
        lose += 1
        if lose == 3:
            print("Game over\n" + str(win))
            break
else:
    print("You won\n" + str(win))
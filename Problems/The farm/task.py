money = int(input())
if money < 23:
    print("None")
elif money in range(23, 678):
    if money // 23 == 1:
        print("1 chicken")
    else:
        print(str(money // 23) + " chickens")
elif money in range(678, 1296):
    if money // 678 == 1:
        print("1 goat")
    else:
        print(str(money // 23) + " goats")
elif money in range(1296, 3848):
    if money // 1296 == 1:
        print("1 pig")
    else:
        print(str(money // 1296) + " pigs")
elif money in range(3848, 6769):
    if money // 3848 == 1:
        print("1 cow")
    else:
        print(str(money // 3848) + " cows")
elif money >= 6769:
    print(str(money // 6769) + " sheep")
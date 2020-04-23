number = int(input())
counter = 0
for n in range(1, number + 1):
    if n < 1:
        print("This number is not prime")
        break
    if number % n == 0:
        counter += 1
        if counter > 2:
            print("This number is not prime")
            break
else:
    if number == 1:
        print("This number is not prime")
    else:
        print("This number is prime")
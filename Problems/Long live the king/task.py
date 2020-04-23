while True:
    try:
        first = int(input())
        second = int(input())
    except ValueError:
        print("Must be a number")
        continue
    if first < 1 or first > 8 or second < 1 or second > 8:
        print("Coordinates are numbers between 1 and 8 inclusively")
    else:
        break
if first in (1, 8) and second in (1, 8):
    print(3)
elif first in (1, 8) or second in (1, 8):
    print(5)
else:
    print(8)

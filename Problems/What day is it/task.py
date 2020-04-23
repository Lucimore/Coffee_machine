number = int(input()) * 60 * 60
now = 10 * 60 * 60 + 30 * 60
if number < 0 and now - abs(number) < 0:
    print("Monday")
elif now + number > 24 * 60 * 60:
    print("Wednesday")
else:
    print("Tuesday")
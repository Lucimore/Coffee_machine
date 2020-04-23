score = float(input())
top = float(input())
grade = score * 100 / top
if top == 0:
    print("Impossible")
elif grade >= 90:
    print('A')
elif 80 <= grade < 90:
    print('B')
elif 70 <= grade < 80:
    print('C')
elif 60 <= grade < 70:
    print('D')
else:
    print('F')
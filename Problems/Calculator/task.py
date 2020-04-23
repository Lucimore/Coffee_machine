# put your python code here
first = float(input())
second = float(input())
action = input()
if action == "+":
    print(first + second)
elif action == "-":
    print(first - second)
elif action == "/":
    if second == 0:
        print("Division by 0!")
    else:
        print(first / second)
elif action == "*":
    print(first * second)
elif action == "mod":
    if second == 0:
        print("Division by 0!")
    else:
        print(int(first) % int(second))
elif action == "pow":
    print(first ** second)
elif action == "div":
    if second == 0:
        print("Division by 0!")
    else:
        print(int(first) // int(second))
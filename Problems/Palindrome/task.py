# put your python code here
word = input()
revword = word[::-1]
if word == revword:
    print("Palindrome")
else:
    print("Not palindrome")
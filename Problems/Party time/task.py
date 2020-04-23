names = []
while True:
    name = input()
    if name != '.':
        names.append(name)
    else:
        print(names)
        print(len(names))
        break

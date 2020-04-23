cafe = []
while True:
    name = input()
    if name == 'MEOW':
        length = len(cafe) - 1
        maximum = cafe[length][1]
        while length != 0:
            if length - 1 >= 0 and int(maximum) < int(cafe[length - 1][1]):
                maximum = cafe[length - 1][1]
            length -= 1
        break
    cafe.append(name.split())
length = len(cafe) - 1
while length != -1:
    if cafe[length][1] == maximum:
        print(cafe[length][0])
    length -= 1
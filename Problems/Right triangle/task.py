class RightTriangle:
    def __init__(self, hyp, leg_1, leg_2):
        self.c = hyp
        self.a = leg_1
        self.b = leg_2
        # calculate the area here
        self.area = 0.5 * self.a * self.b


sides = input().split()
triangle = RightTriangle(int(sides[0]), int(sides[1]), int(sides[2]))
if triangle.c ** 2 == triangle.a ** 2 + triangle.b ** 2:
    print(triangle.area)
else:
    print("Not right")

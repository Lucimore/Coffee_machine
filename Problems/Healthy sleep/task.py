minimum = int(input())
maximum = int(input())
real = int(input())
if real < minimum:
    print("Deficiency")
elif real > maximum:
    print("Excess")
else:
    print("Normal")
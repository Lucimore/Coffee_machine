age = int(input())
if age <= 16:
    print("Lion King")
elif age in range(17, 26):
    print("Trainspotting")
elif age in range(26, 41):
    print("Matrix")
elif age in range(41, 61):
    print("Pulp Fiction")
else:
    print("Breakfast at Tiffany's")
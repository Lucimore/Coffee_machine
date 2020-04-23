army = int(input())
if army < 1:
    print("no army")
elif army in range(1, 10):
    print("few")
elif army in range(10, 50):
    print("pack")
elif army in range(50, 500):
    print("horde")
elif army in range(500, 1000):
    print("swarm")
elif army >= 1000:
    print("legion")

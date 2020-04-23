numbers = [int(x) for x in input().split()]
total = 0
for num in numbers:
    total += num
print(total / len(numbers))

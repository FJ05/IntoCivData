def sumN(n):
    sum = 0
    for x in range(n + 1):
        sum = sum + x
    return sum

def sumNCubes(n):
    sum = 0
    for x in range(n + 1):
        sum = sum + x**2
    return sum

print(sumN(int(input("Enter a number for the sum of the first n natural numbers: "))))
print(sumNCubes(int(input("Enter a number for the sum of the cubes of the first n natural numbers: "))))

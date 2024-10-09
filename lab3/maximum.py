def find_the_largest(number1:int, number2:int, number3:int):
    if number1 > number2 and number1 > number3:
        return f"{number1} is the largest number"
    elif number2 > number3:
        return f"{number2} is the largest number"
    else:
        return f"{number3} is the largest number"

print(find_the_largest(int(input("Enter nr1: ")), int(input("Enter nr2: ")), int(input("Enter nr3: "))))
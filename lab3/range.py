def check_if_in_range(start:int, end:int, number:int):
    if end < start:
        return "💀"
    if number <= end and number >= start:
        return f"The number {number} is in the range {start}-{end}"
    else:
        return f"The number {number} is NOT in the range {start}-{end}"
    
start = int(input("Enter the starting value of the range: "))
end = int(input("Enter the ending value of the range: "))
number = int(input("Enter the number that you want to check if it is in the range: "))

print(check_if_in_range(start, end, number))
def list_multiplier(list):
    sum = 1
    for entry in list:
        sum = sum * entry
    return sum

print(list_multiplier([1,2,3,4,5,6,7,8,9,10]))

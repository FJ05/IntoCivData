import math

def handler(first, *args_):
    args = list(args_) # convert from tuple to list
    maximum = args[0] # for assuming that the fist in args is the maximum
    median = 0 # placeholder of the median
    args.sort() # will come handy when looking for median
    first_in_list = False # assuming that the first is not in args
    print(len(args) + 1)

    for arg in args: # look for the maximum in args
        if arg > maximum:
            maximum = arg

    average = sum(args) / len(args)
    
    if len(args) % 2 == 1: # if the sum of arguments is odd
        median = args[len(args) // 2] # this is the middle of args
    else: # if the sum of arguments is even
        index = len(args) // 2
        median = (args[index - 1] + args[index]) / 2

    for arg in args:
        if arg == first:
            first_in_list = True

    return maximum, average, median, first_in_list

maximum, average, median, first_in_list = handler(9,7,6,2,3,4,5,9)
print(f"The maximum value is: {maximum}\nThe average value is {average}\nThe median value is {median}\nThe first number in the input is also present in the set of other arguments: {first_in_list}")

# Given an array of integers as strings and numbers, return the sum of the array values as if all were numbers.

# Return your answer as a number.

def sum_mix(arr):
    total = 0
    for x in arr:
        total += int(x)
    return total


#--------------------

def sum_mix(arr):
    return sum(int(x) for x in arr)


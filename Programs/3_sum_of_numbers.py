# Given two integers a and b, which can be positive or negative, find the sum of all the integers between and including them and return it. If the two numbers are equal return a or b.

# Note: a and b are not ordered!
# Examples (a, b) --> output (explanation)

# (1, 0) --> 1 (1 + 0 = 1)
# (1, 2) --> 3 (1 + 2 = 3)
# (0, 1) --> 1 (0 + 1 = 1)
# (1, 1) --> 1 (1 since both are same)
# (-1, 0) --> -1 (-1 + 0 = -1)
# (-1, 2) --> 2 (-1 + 0 + 1 + 2 = 2)

def get_sum(a, b):
    # Find the smaller and larger number
    start = min(a, b)
    end = max(a, b)
    
    # Use the built-in sum and range functions to calculate the total
    return sum(range(start, end + 1))

#-----------------------------------------------------#

def get_sum(a, b):
    # If both numbers are the same, return either
    if a == b:
        return a

    # Find the smaller and larger number
    if a < b:
        start = a
        end = b
    else:
        start = b
        end = a

    # Manually calculate the sum
    total = 0
    for i in range(start, end + 1):
        total += i

    return total

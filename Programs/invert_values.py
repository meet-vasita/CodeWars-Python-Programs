# Given a set of numbers, return the additive inverse of each. Each positive becomes negatives, and the negatives become positives.

# [1, 2, 3, 4, 5] --> [-1, -2, -3, -4, -5]
# [1, -2, 3, -4, 5] --> [-1, 2, -3, 4, -5]
# [] --> []

def invert(lst):
    inv_lst = []
    for i in lst:
        inv_lst.append(-i)
    return inv_lst

print(invert([1,2,3,4,5]))

#List Comprehension

def invert(lst):
    l = [-i for i in lst]
    return (l)


print(invert([1,-2,3,-4]))
# You will be given an array a and a value x. All you need to do is check whether the provided array contains the value.

# a can contain numbers or strings. x can be either.

# Return true if the array contains the value, false if not.

def check(seq, elem):
    for i in seq:
        if i == elem:
            return True
    return False
        
# ------------------

def check(seq,elem):
    return elem in seq

        


print(check([1,2,3,4,5],4))
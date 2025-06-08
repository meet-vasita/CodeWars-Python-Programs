# An isogram is a word that has no repeating letters, consecutive or non-consecutive. Implement a function that determines whether a string that contains only letters is an isogram. Assume the empty string is an isogram. Ignore letter case.

# Example: (Input --> Output)

# "Dermatoglyphics" --> true
# "aba" --> false
# "moOse" --> false (ignore letter case)


def is_isogram(string):
    string = string.lower()
    seen_letters = "" 

    for letter in string:
        if letter in seen_letters:
            return False
        seen_letters += letter  
    
    return True


print(is_isogram('Meet'))

#Much Better Code
def is_isogram(string):
    return len(string) == len(set(string.lower()))


'''
input string: 'Meet'
string.lower: 'meet'
seen letter = ''

m
e
e
t

First iteration: Check if 'm' is in seen_letters (''): No, so add 'm' to seen_letters → seen_letters = 'm'.

Second iteration: Check if 'e' is in seen_letters ('m'): No, so add 'e' to seen_letters → seen_letters = 'me'.

Third iteration: Check if 'e' is in seen_letters ('me'): Yes, so return False immediately.

Fourth iteration: Would check 't' if the function hadn't returned False in the third iteration, but it's skipped.

The program would never make it to the 4th iteration because of the early exit on the 3rd iteration.
'''
# We need a function that can transform a number (integer) into a string.

# What ways of achieving this do you know?
# Examples (input --> output):

# 123  --> "123"
# 999  --> "999"
# -100 --> "-100"


def number_to_string(num):
    num_to_str = str(num)
    return num_to_str

n_to_s = number_to_string(123)
print(type(n_to_s))

# -------

def number_to_string(n):
  return str(n)
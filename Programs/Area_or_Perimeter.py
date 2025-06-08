# You are given the length and width of a 4-sided polygon. The polygon can either be a rectangle or a square.
# If it is a square, return its area. If it is a rectangle, return its perimeter.

# Example(Input1, Input2 --> Output):

# 6, 10 --> 32
# 3, 3 --> 9

def area_or_perimeter(l , w):
    
    area_of_square = l*w
    perimeter_of_rectangle = 2 * (l+w)
    
    if l == w:
        return area_of_square
    
    return perimeter_of_rectangle


print(area_or_perimeter(4,4))
print(area_or_perimeter(6,10))

# Much Better Code
def area_or_perimeter(l , w):
    return l * w if l == w else 2 * (l + w)
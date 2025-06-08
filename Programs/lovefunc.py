#Timmy & Sarah think they are in love, but around where they live, they will only know once they pick a flower each. If one of the flowers has an even number of petals and the other has an odd number of petals it means they are in love.

#Write a function that will take the number of petals of each flower and return true if they are in love and false if they aren't.

#Beginner Level Code
def lovefunc(flower1,flower2):
    if (flower1 % 2 == 0 or flower2 % 2 == 1) and (flower1 % 2 == 1 or flower2 % 2 == 0):
        return True
    else:
        return False

print(lovefunc(2,4))


#Much Better Code
def lovefunc(flower1,flower2):
    return (flower1 % 2) != (flower2 % 2)


print(lovefunc(2,4))
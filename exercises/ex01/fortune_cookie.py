"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730315718"

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 
from random import randint


# Begin your solution here...

random_int: int = randint(0, 3)

print("Your fortune cookie says...")
if random_int == 0:
    print("Just one more episode, because you deserve it.")
else:
    if random_int == 1:
        print("You will pass all your classes this semester and forward.")
    else:
        if random_int == 2:
            print("Get that bag. Treat yourself.")
        else:
            if random_int == 3:
                print("Look up and forward, no matter how hard it gets.")
print("Now, go spread positive vibes!")
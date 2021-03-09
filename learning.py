import random
import sys

def dn(n): #a die with n sides
    return random.randrange(1, n+1)

def xdn(x, n): #x dice with n sides
    total = 0
    dice = []
    for i in range(x):
        ret = dn(n)
        total = total + ret
        dice.append(ret)
    string_ints = [str(int) for int in dice] #this creates a new variable string_ints, and initializes it by taking every int in dice and converting it to a string
    return("Sum: " + str(total) + ". Dice: " + ", ".join(string_ints))


x = int(sys.argv[1]) #sys.argv[] is the inputs from the commmand line
n = int(sys.argv[2])
print(xdn(x,n))

#todo: implement edge case handling

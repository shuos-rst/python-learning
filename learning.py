# we out here learning
import random

def dn(n): #a die with n sides
    if (n > 10000) or (n <= 0): #edge case handling. fix this to have proper try/except handling
        return 
    die = 1/n
    a = random.random()
    return (int((a // die) + 1))

def xdn(x, n): #x dice with n sides
    out = 0
    for i in range(x):
        out = out + dn(n)
    return(out)



for x in range (1):
    print(xdn(2,0))

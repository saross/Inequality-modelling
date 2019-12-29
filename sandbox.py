# Sandbox for experimenting with monte carlo simulations
#
#
# Load libraries
import numpy
import random

# Learn basics of monte carlo simulations, starting with gambling with dice
# https://pythonprogramming.net/monte-carlo-simulator-python/

# Create dice

def rollDice():
    roll = random.randint(1,100)
    return roll

# Roll dice 100 times and print all rolls

x = 0
while x < 100:
    result =rollDice()
    print(result)
    x=x+1

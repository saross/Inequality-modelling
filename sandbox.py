###########################################################
# Sandbox for experimenting with monte carlo simulations
###########################################################
#
# Load libraries

import numpy
import random

# Learn basics of monte carlo simulations, starting with gambling with dice
# https://pythonprogramming.net/monte-carlo-simulator-python/

# # Create dice
#
# def rollDice():
#     roll = random.randint(1,100)
#     return roll
#
# # Roll dice 100 times and print all rolls
#
# x = 0
# while x < 100:
#     result =rollDice()
#     print(result)
#     x = x+1

# Change to simple win-loss

def rollDice():
    roll = random.randint(1,100)

    if roll == 100:
        print(roll, 'loss')
        return False
    elif roll <= 50:
        print(roll, 'loss')
        return False
    elif 100 > roll >= 51:
        print(roll,'win')
        return True

# Create a simple bettor, betting the same amount each time

def simple_bettor(funds, initial_wager, wager_count):
    value = funds
    wager = initial_wager

    currentWager = 0

    while currentWager < wager_count:
        if rollDice():
            value = value+wager
        else:
            value = value-wager

        currentWager = currentWager+1
        print('Funds:', value)

simple_bettor(10000,100,100)

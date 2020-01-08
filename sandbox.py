###########################################################
# Sandbox for experimenting with monte carlo simulations
###########################################################
#
# Load libraries

import random
import matplotlib
import matplotlib.pyplot as plt
import numpy

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
        #print(roll, 'roll was 100, loss')
        return False
    elif roll <= 50:
        #print(roll, 'roll was <50, loss')
        return False
    elif 100 > roll > 50:
        #print(roll,'roll was 51-99, win')
        return True

# Create a simple bettor, betting the same amount each time

def simple_bettor(funds, initial_wager, wager_count):
    value = funds
    wager = initial_wager

    # make wager number the x variable

    xWager = []

    # make value (funds balance) the Y variable

    yValue = []


    currentWager = 1 # start at 1 and not 0 for first wager

    while currentWager <= wager_count:
        if rollDice():
            value = value + wager
            # append current wager count and new value (funds balance) if bet is successful
            xWager.append(currentWager)
            yValue.append(value)

        else:
            value = value-wager
            # append current wager count and new value (funds blance) if bet is unsuccessful
            xWager.append(currentWager)
            yValue.append(value)

        currentWager = currentWager + 1

# Exit out if funds ever fall to zero

    # if value <= 0:
    #     value = 'Broke!'
    #     print('Funds:', value)

# If bettor survives all rounds, print fund balance

    # print('Funds:', value)

    plt.plot(xWager,yValue)

# Now run lots of wagers

x = 0
while x < 100:
    simple_bettor(10000,100,50)
    x += 1

plt.ylabel('Account Balance')
plt.xlabel('Wager Count')
plt.show()
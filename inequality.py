###########################################################
# Experiments with monte carlo simulations of equality
###########################################################
#
# Load libraries

import random
import matplotlib
import matplotlib.pyplot as plt
import numpy

# Create random annual gain / loss of 100 arbitrary units

def rollDice():
    roll = random.randint(-100,100)
    return roll

# Create a simple model household

def household(wealth, year_count):
	value = wealth
	year = year_count

    # make year the x variable

    xYear = []

    # make wealth the Y variable

    yWealth = []


    currentYear = 1 # start at Year

    while currentYear <= year:
    	rollDice()
    	value = value + roll
    	# append current year count and new wealth to table
    	xYear.append(year)
    	yWealth.append(value)

        currentYear += 1 # increment year by 1


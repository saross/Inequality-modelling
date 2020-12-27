###########################################################
# Experiments with monte carlo simulations of equality
###########################################################
#
# Load libraries

import matplotlib
import matplotlib.pyplot as plt
import numpy as np

# Create random annual gain / loss figure between -100 and +100 arbitrary units

def rollDice():
	roll = np.random.randint(-100,101)
	return roll

# Create a simple model household
def household(wealth, year_count):
	value = wealth

	xYear = np.empty([1]) # make year the x variable
	yWealth = np.empty([1]) # make wealth the Y variable

	currentYear = 0 # start at Year 0 (initial state)

	while currentYear <= year_count:
		# append current year count and new wealth to table
		np.append(xYear, [currentYear])
		np.append(yWealth, [value])

		result = rollDice() # generate random gain or loss
		value = value + result # adjust household wealth by the gain or loss for the year

		currentYear += 1 # increment year by 1

	plt.plot(xYear,yWealth)

# Now generate multiple households
i = 1
while i <= 100:
	household(1000, 25)
	i += 1

plt.ylabel('Household wealth')
plt.xlabel('Year')
plt.show()
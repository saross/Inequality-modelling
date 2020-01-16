##############################################
#
# Tests of things that don't work
#
##############################################

import numpy as np

y = np.empty([2])

x = np.append(y, [2, 3])

print(x)

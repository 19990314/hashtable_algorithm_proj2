# ------------------------------------------------------------------------
# This module is used for generating testing cases.
#
# Author: Shuting Chen
# Date Created: 10/28/2022
# Date Last Modified: 11/8/2022
# ------------------------------------------------------------------------

import random

# modify n here
n = 120
#input_size = [36, 84, 108, 40, 80, 120]
input_size = [36, 84, 108]

# generate files containing different cases
for size in input_size:
    f = open("/Users/iris/Desktop/project2/inputs/input_" + str(size) + ".txt", "w")
    f.write("605.420 Algorithms of Bioinformatics	            Project 2\n\n")
    # generate numbers
    for i in range(0, size):
        f.write(str(random.randint(1000, 99999)) + "\n")
f.close()
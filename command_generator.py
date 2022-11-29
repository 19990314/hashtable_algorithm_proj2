# ------------------------------------------------------------------------
# This module is used for generating commands for all the test cases and
# corresponding test cases.
#
# Author: Shuting Chen
# Date Created: 09/22/2022
# Date Last Modified: 09/25/2022
# ------------------------------------------------------------------------

input_size = [36, 84, 108, 40, 80, 120]
collision_strategy = ["linear", "quadratic", "chaining"]
tablesize = 120
bucket_size = [1, 3]
modulo = [41, 113, 120]

import os


def test_command(command_line):
    """
        test the command line generated

        Return:
            none
    """
    try:
        os.system(t4)
    except TypeError as ve:
        print(t4)


# generate commands
for i in input_size:
    t1 = "python3.10 main.py /Users/iris/Desktop/project2/inputs/input_" + str(i) + ".txt "
    for j in modulo:
        # output file path + name:
        #t2 = t1 + "/Users/iris/Desktop/project2/output/my_outputs/multiply_tests/k" + str(i) + "_m" + str(j)
        t2 = t1 + "/Users/iris/Desktop/project2/output/my_outputs/k" + str(i) + "_m" + str(j)
        for k in bucket_size:
            t3 = t2 + "_b" + str(k)
            for q in collision_strategy:
                if j == 41 and q == "chaining":
                    continue
                if j == 41 and k == 1:
                    continue
                if k == 3 and j != 41:
                    continue
                else:
                    t4 = t3 + "_" + q
                    # t4 += ".txt " + str(j) + " " + str(k) + " " + str(q) + " mul"
                    t4 += ".txt " + str(j) + " " + str(k) + " " + str(q)
                    print(t4)
                    # call every test cases from command line
                    #test_command(t4)

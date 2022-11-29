# ------------------------------------------------------------------------
# This module handle I/O functions for Project 2.
#
# Author: Shuting Chen
# Date Created: 10/28/2022
# Date Last Modified: 11/8/2022
# ------------------------------------------------------------------------

import os


def read_input(filename):
    try:
        if os.stat(filename).st_size == 0:
            print("Empty File! Please check file content.")
            exit(0)
    except FileNotFoundError as file_error:
        print("Cannot find the File! Please check file path:" + filename)
        exit(0)

    # read input file, save matrices into matrices_container
    matrices_container = []
    with open(filename, encoding='utf8') as f:
        input = []
        # process matrix line by line
        for line in f:
            if len(line.split(' ')) == 1 and line != '\n':
                input.append(int(line))
    return input


def output_generator(filepath, input_size, table_size, inputs, hashtable_info):
    f = open(filepath, "w")
    f.write("Input size: " + str(input_size) + "\n")
    f.write("Input keys: \n")
    line = []
    int_ct = 0
    for i in inputs:
        line.append(str(i))
        int_ct += 1
        if int_ct == 5:
            f.write('    '.join(line) + "\n")
            line = []
            int_ct = 0
    f.write('    '.join(line) + "\n")

    f.write("\n-----------------------------------------------\n")
    f.write(hashtable_info)
    f.close()

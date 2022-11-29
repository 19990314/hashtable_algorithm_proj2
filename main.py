# ------------------------------------------------------------------------
# This module is the main file for Project 2, providing the main steps of
# hash table and testing.
#
# Author: Shuting Chen
# Date Created: 10/28/2022
# Date Last Modified: 11/8/2022
# ------------------------------------------------------------------------

import sys
import os
from IO_tools import *
from hashtable import HashTable

if __name__ == "__main__":

    # input and output parameters
    numbers = read_input(sys.argv[1])
    output_file_path = sys.argv[2]

    # other parameters:
    tablesize = 120
    modulo = int(sys.argv[3])
    bucket_size = sys.argv[4]
    collisionscheme = sys.argv[5]

    # optional parameters: c1, c2, and modulo_scheme
    c1 = 0.5
    c2 = 0.5
    if len(sys.argv) == 8 and collisionscheme == "quadratic":
        c1 = float(sys.argv[6])
        c2 = float(sys.argv[7])
    modulo_scheme = "div"
    if len(sys.argv) == 6:
        if sys.argv[5] == "mul":
            modulo_scheme = "mul"

    # declare hash table
    hashtable = HashTable(table_size=tablesize, bucket_size=int(bucket_size),
                          collision_scheme=collisionscheme, modulo_scheme=modulo_scheme)

    # insert values
    for i in numbers:
        hashtable.insert(i, modulo, c1, c2)

    # output results
    output_generator(output_file_path, len(numbers), hashtable.table_size, numbers,
                     hashtable.print_table_info(len(numbers), modulo))


==========================================Project 2 Hash Table====================================================
==================================================README==========================================================
[Command line]
python3 main.py input_file output_file modulo bucket collision_scheme hash_scheme c1 c2

[Parameters]
    input_file: the absolute path of input file
    output_file: the absolute path of output file
    modulo: the modulo value
    bucket: the bucket size
    collision_scheme*: linear/quadratic/chaining
    * parameter input can be any of: "linear", "linear probing", "quadratic",
                            "quadratic probing", or "chaining" (case insensitive)
    hash_scheme*: [optional] multiplication/division
    c1: [optional] c1 value used for quadratic probing
    c2: [optional] c2 value used for quadratic probing
    * parameter input can be any of: "mul" or "div"

[Note]
    1. c1 and c2 are optional parameters for quadratic probing. If collision_scheme = "quadratic" and parameters
    of c1 and c2 are empty, then my default values are c1=0.5 and c2=0.5.
    2. If hash_scheme != "mul", then c1 and c2 should never be given in the command line.

[example 1]
python3 main.py /Users/iris/Desktop/project2/inputs/input_36.txt
                     /Users/iris/Desktop/project2/output/my_outputs/k36_m41_b3_linear.txt 41 3 linear mul

[example 2: extra tests for c1 and c2]
python3 main.py /Users/iris/Desktop/project2/inputs/input_84.txt
                    /Users/iris/Desktop/project2/output/my_outputs/c1c2_tests/k84_m113_b1_quadratic_0.9_0.5.txt
                            113 1 quadratic 0.9 0.5

===============================================================================================================
[Filename formats]
My input files are in: ./project2/inputs/
Input filenames are input_n.txt where n is the input size, eg., input_36.txt means input file with 36 input values

My output files (by division scheme) are in: ./project2/output/my_outputs/
Output files (by multiplication scheme) are in: ./project2/output/my_outputs/multiply_tests
Input filenames are ki_mj_bp_q.txt, eg., k36_m41_b3_linear.txt.
    * i is the input size, j is the modulo value, p is the bucket size, and q is the collision scheme

[Input]
A text document with strings and integers.
As long as integers are placed each at a line, another verbose text lines and blank lines will be ignored.

[Output]
Input size: 36
Input keys:
99494    62767    34250    98639    9885
66579    22167    55854    96855    80935
[...skipped...]

-----------------------------------------------
Method: division mod113
Hash Table size: 120
	bucket size: 1
Collision handling scheme: linear
	primary collisions: 5
	secondary collisions: 0
	total collisions: 5
Keys not inserted: []
Load factor: 0.3
Hash table:
----    ----    ----    41248    ----
----    19329    ----    ----    ----
----    34250    ----    ----    96855
[...skipped...]

===============================================================================================================
[Extra code not required in our project2]
command_generator.py: Since this project needs a lot of test case to analyze the performance. I wrote a python
file to generate command lines for each pair of input and output with different parameters.

input_generator.py: Generate input files by a given input size parameter

========================================================END=======================================================

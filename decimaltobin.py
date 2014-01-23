"""Sample code to read in test cases:"""

import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases.readlines():
    # ignore test if it is an empty line
    # 'test' represents the test case, do something with it
    if test:
        N = int(test)
        print bin(N).replace('0b','')

test_cases.close()

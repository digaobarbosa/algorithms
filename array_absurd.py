"""Sample code to read in test cases:"""

import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases.readlines():
    test = test.strip()
    if not test:
        continue
    N,line = test.split(';')
    N = int(N)
    array = line.split(',')
    array = [int(a) for a in array]
    S = (N-2)*(N-1)/2
    Sarray = sum(array)
    print Sarray-S

test_cases.close()

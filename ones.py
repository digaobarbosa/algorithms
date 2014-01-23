"""Sample code to read in test cases:"""

import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases.readlines():
    number = int(test)
    mask=1
    count=0
    while mask<=number:
        if mask & number:
            count+=1
        mask = mask<<1
    print count

test_cases.close()

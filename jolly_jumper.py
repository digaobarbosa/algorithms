"""Sample code to read in test cases:"""

import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases.readlines():
    # ignore test if it is an empty line
    # 'test' represents the test case, do something with it
    # ...
    # ...
    numbers = [int(j) for j in test.split()[1:]]
    if len(numbers)==1:
        print 'Jolly'
        continue
    marks = [0 for a in xrange(len(numbers))]
    i=1
    ok = True
    while i<len(numbers) and ok:
        r = abs(numbers[i]-numbers[i-1])
        if r<len(marks) and marks[r]==0:
            marks[r]=1
        else:
            ok=False
        i+=1
    print ok and 'Jolly' or 'Not Jolly'

test_cases.close()

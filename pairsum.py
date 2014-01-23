"""Sample code to read in test cases:"""

import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases.readlines():
    # ignore test if it is an empty line
    # 'test' represents the test case, do something with it
    # ...
    if test:
        line,N = test.split(';')
        N = int(N)
        array = [int(a) for a in line.split(',')]
        array.sort()
        last = len(array)-1
        first=0
        pairs =[]
        while first<last:
            a = array[first]
            b = array[last]
            s=a+b
            if s==N:
                pairs.append((a,b))
                first+=1
                last-=1
            elif s>N:
                last-=1
            else:
                first+=1
        if pairs:
            pairs.sort()
            print ';'.join(['%d,%d'%a for a in pairs])
        else:
            print 'NULL'



test_cases.close()

__author__ = 'digao'
from StringIO import StringIO
import sys
import collections


def solve(line):
    letters = collections.defaultdict(lambda : 0)
    for c in line:
        letters[c] += 1
    l = len(line)
    if l%2==0:
        impares = [a for a in letters.values() if a%2 != 0]
        print impares and 'NO' or 'YES'
    else:
        impares = [a for a in letters.values() if a%2 != 0 ]
        print len(impares)!=1 and 'NO' or 'YES'



def main(input):
    for line in input.readlines():
            solve(line.strip())

test_input = """aaabbbb
cdefghmnopqrstuvw
"""

main(StringIO(test_input))
#main(sys.stdin)


"""
xy%N=0
(x+y)=k

2
2
3 4 6
7 8 9 10 12 15 18 24 42
25
0 - 1 - (2,2)
1 - 1 - (2,2)
2(x+y) =xy - (3,6),(4,4),(6,3)
6(x+y) = xy - (7,42), (8,24),(9,18),(10,15),(12,12),(15,10),(18,9),(24,8),(42,7)
24(x+y) = xy - (25,25*24),(26,24*13),(27,24*9),(28,6*28),(30,120),(32.96),(33,88),(36,72),(40,60),(42,14*8)

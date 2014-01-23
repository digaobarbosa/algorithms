__author__ = 'digao'
import sys

def solve(line):
    n,p1,p2 = (int(a) for a in line.split(','))
    p1r = n&(1<<(p1-1))>0
    p2r = n&(1<<(p2-1))>0
    res = str(p1r == p2r).lower()
    print res


input = sys.stdin
if sys.argv[1]:
    input = open(sys.argv[1], 'r')

lines = input.readlines()
for line in lines:
    solve(line.strip())


input.close()
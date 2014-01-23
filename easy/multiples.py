__author__ = 'digao'
import sys

def solve(line):
    x,n = (int(a) for a in line.split(','))
    if x%n==0:
        print x/n
    else:
        print (x/n+1)*n


input = sys.stdin
if sys.argv[1]:
    input = open(sys.argv[1], 'r')

lines = input.readlines()
for line in lines:
    solve(line.strip())


input.close()
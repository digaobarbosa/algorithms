__author__ = 'digao'
import sys
import re
def solve(line):
    S,reg = line.split(',')
    reg = reg.replace('\*','#').replace('*','.*').replace('#','\*')
    if re.findall(reg,S):
        print 'true'
    else:
        print 'false'


input = sys.stdin
if sys.argv[1]:
    input = open(sys.argv[1], 'r')

lines = input.readlines()
for line in lines:
    solve(line.strip())


input.close()
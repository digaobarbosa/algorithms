__author__ = 'digao'
import sys

def solve(line):
    if not line:
        return
    base,repls = line.split(';')
    repls = repls.split(',')
    res = base
    array = [0 for i in xrange(len(base))]
    for i in xrange(0,len(repls),2):
        r = repls[i]
        rr = repls[i+1]
        count = res.count(r)
        start=0
        while count:
            index = res.find(r,start)
            if index>=0 and 1 not in array[index:index+len(r)]:
                res = res[:start]+res[start:].replace(r,rr,1)
                array = array[:index]+[1 for _a in xrange(len(rr))]+array[index+len(r):]
                count = res.count(r)
            else:
                count-=1
            start=index+1

    print res


input = sys.stdin
if sys.argv[1]:
    input = open(sys.argv[1], 'r')

lines = input.readlines()
for line in lines:
    solve(line)
input.close()
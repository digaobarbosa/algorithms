__author__ = 'digao'
import sys
from  collections import namedtuple
import math

Point = namedtuple('Point',['x','y'])
def solve(points):
    points.sort()
    minimum = 100000000
    for i in xrange(len(points)):
        p = points[i]
        for j in xrange(i+1,len(points)):
            q = points[j]
            dist = math.pow(p.x-q.x,2)+math.pow(p.y-q.y,2)
            if dist<minimum:
                minimum=dist
    if minimum == 100000000:
        print 'INFINITY'
    else:
        print '%.4f'%math.sqrt(minimum)

input = sys.stdin
if sys.argv[1]:
    input = open(sys.argv[1], 'r')

N = int(input.readline().strip())
while N:
    points = []
    for i in xrange(N):
        x,y = (int(p) for p in input.readline().split())
        points.append(Point(x,y))
    solve(points)
    N = int(input.readline().strip())


input.close()
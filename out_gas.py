__author__ = 'digao'
import math

a²t/2+vt = D

def respToA(a,other,D):

    possible = [(t,p) for (t,p) in other if p<D]
    if possible and len(other)>len(possible):
        (at,ap)=other[len(possible)]
        (bt,bp) = possible[-1]
        v = (ap-bp)/(at-bt)
        timeo = D==ap and at or bt + (D-bp)/v
        lastp,lastt,lastv = 0,0,0

        lastot,lastop=-1,0
        timea=0
        for (ot,op) in other:
            tt = lastt + math.sqrt(2*(op-lastp)/a)
            if tt<ot:
                lastp=op
                lastt=ot
                lastv= lastot >=0 and (op-lastop)/(ot-lastot) or 0
            if op>=D:
                timea = tt
            lastot=ot
            lastop=op

        return timea< timeo and '%.7f'%timeo or '%.7f'%timea
    else:
        timea = math.sqrt(2*D/a)
        return '%.7f'%timea


import sys
input = sys.stdin
if sys.argv[1]:
    input = open(sys.argv[1], 'r')
TESTS = int(input.readline())
out = open('out','w')
for i in xrange(TESTS):
    D,N,A = [a for a in input.readline().split()]
    D = float(D)
    other = []
    for j in xrange(int(N)):
        t,p = [float(a) for a in input.readline().split()]
        other.append((t,p))
    A = [float(a) for a in input.readline().split()]
    s = 'Case #%d: '%(i+1)
    print s
    out.write(s+'\n')
    for a in A:
        s = respToA(a,other,D)
        print s
        out.write(s+'\n')
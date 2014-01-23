__author__ = 'digao'
import sys

R,D,L,U = 0,1,2,3
def incr(i,j,op,round,n,m):
    r = None
    bop = op
    if op==R:
        if i<m-round-1:
            i+=1
            r = (i,j,op,round)

        else:
            op = D
    if op==D:
        if j<n-round-1:
            j+=1
            r = (i,j,op,round)
        else:
            op = L
    if op==L:
        if bop==R:
            return None
        elif i>round:
            i-=1
            r = (i,j,op,round)
        else:
            op=U
    if op==U:
        if bop==D:
            return None
        elif j>round+1:
            j-=1
            r = (i,j,op,round)

        else:
            op=R
            round+=1
            if bop==L:
                return None
            if i<m-round-1 and round<n-1:
                i+=1
                r = (i,j,op,round)

    return r







def solve(line):
    if not line:
        return
    n,m,els = line.strip().split(';')
    n = int(n)
    m=int(m)
    els = [e.strip() for e in els.split(' ')]
    state = (0,0,0,0)
    res = ''
    while state is not None:
        i,j,op,round = state
        res+=els[j*m+i]+' '
        state = incr(state[0],state[1],state[2],state[3],n,m)
    print res.strip()









input = sys.stdin
if sys.argv[1]:
    input = open(sys.argv[1], 'r')

lines = input.readlines()
for line in lines:
    solve(line)
input.close()
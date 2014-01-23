__author__ = 'digao'
import sys


digits = {'1':('1',),'0':('0',),
          '2':('a','b','c'),
          '3':('d','e','f'),
          '4':('g','h','i'),
          '5':('j','k','l'),
          '6':('m','n','o'),
          '7':('p','q','r','s'),
          '8':('t','u','v'),
          '9':('w','x','y','z')
}

def all_combs(line):
    res = []
    if len(line)==1:
        return list(digits[line])
    for c in digits[line[0]]:
        combs = all_combs(line[1:])
        res.extend([c+comb for comb in combs])
    return res


def solve(line):
    if not line:
        return
    res = all_combs(line)
    print ','.join(res)

input = sys.stdin
if sys.argv[1]:
    input = open(sys.argv[1], 'r')

lines = input.readlines()
for line in lines:
    solve(line.strip())
input.close()
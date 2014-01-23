__author__ = 'digao'
from collections import defaultdict
import sys
import re

def rec_depth(graph,k,seen,parents,cycles):
    parents.append(k)
    seen.add(k)
    for other in graph[k]:
        if len(parents)>1 and other in parents:
            index = parents.index(other)
            if index < len(parents)-2:
                cycles.add(frozenset(parents[index:]))
        else:
            rec_depth(graph,other,seen,parents,cycles)

def depth_cycles(graph):
    seen = set()
    cycles = set()
    for k,v in graph.items():
        if k in seen:
            continue
        rec_depth(graph,k,seen,[],cycles)
    return cycles


input = sys.stdin
if sys.argv[1]:
    input = open(sys.argv[1], 'r')

seen = set()
graph = defaultdict(lambda:set())
lines = input.readlines()
for line in lines:
    time,u1,u2 = (s.strip() for s in line.split('\t'))
    if (u2,u1) in seen:
        graph[u1].add(u2)
        graph[u2].add(u1)
    else:
        seen.add((u1,u2))
cycles = depth_cycles(graph)
result = []
for c in cycles:
    result.append(sorted(tuple(c)))
result.sort()
for res in result:
    print ','.join(res)



input.close()
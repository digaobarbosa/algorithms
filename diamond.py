__author__ = 'digao'

def search_diamond(graph):

    for i in xrange(len(graph)):
        inherits = list(graph[i])
        visited = set()
        while inherits:
            el = inherits.pop()
            if el in visited:
                return True
            visited.add(el)
            inherits.extend(graph[el])
    return False



import sys
test_cases = sys.stdin
if sys.argv[1]:
    test_cases = open(sys.argv[1], 'r')
N = int(test_cases.readline())
out = open('out','w')
for i in xrange(N):
    classes = int(test_cases.readline())
    graph = [[]]
    for j in xrange(classes):
         graph.append([int(a) for a in test_cases.readline().split()][1:])
    diamond = search_diamond(graph)

    res = 'Case #%d: %s'%(i+1,diamond and 'Yes' or 'No')
    print res
    out.write(res+"\n")


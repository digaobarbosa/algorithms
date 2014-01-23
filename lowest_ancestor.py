"""Sample code to read in test cases:"""

class Node:
    def __init__(self,v):
        self.value = v
        self.left =None
        self.right = None

root = Node(30)
root.left = Node(8)
root.right = Node(52)
n20 = Node(20)
n20.right = Node(29)
n20.left = Node(10)
root.left.right=n20
root.left.left = Node(3)

def search(n,node,res=None):
    if node is None: return None
    if res is None: res = []
    res.append(node.value)
    if node.value == n:
        return res
    r = search(n,node.left,res)
    if r: return r
    r = search(n,node.right,res)
    if r: return r
    res.pop()
    return None



import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    A,B = (int(n) for n in test.split())
    l1 = search(A,root)
    l2 = search(B,root)
    l2 = [l for l in l2 if l in l1]
    print l2.pop()





    # ignore test if it is an empty line
    # 'test' represents the test case, do something with it
    # ...
    # ...

test_cases.close()
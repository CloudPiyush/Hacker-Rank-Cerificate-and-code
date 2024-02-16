import math
import os
import random
import re
import sys



class Multiset(object):
    
    def __init__(self):
        self.items = []

    def add(self, val):
        self.items.append(val)
        pass

    def remove(self, val):
        if len(self.items):
            if val in self.items:
                self.items.remove(val)
        pass
    
    def __contains__(self, val):
        if val in self.items:
            return True
        return False
    
    def __len__(self):
        # returns the number of elements in the multiset
        return len(self.items)

if __name__ == '__main__':
    def performOperations(operations):
        m = Multiset()
        result = []
        for op_str in operations:
            elems = op_str.split()
            if elems[0] == 'size':
                result.append(len(m))
            else:
                op, val = elems[0], int(elems[1])
                if op == 'query':
                    result.append(val in m)
                elif op == 'add':
                    m.add(val)
                elif op == 'remove':
                    m.remove(val)
        return result

    q = int(raw_input())
    operations = []
    for _ in xrange(q):
        operations.append(raw_input())

    result = performOperations(operations)
    
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')
    fptr.close()
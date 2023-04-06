import re

class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        if not (8 <= len(A) <= 15):
            return 0
        if not re.search("[0-9]", A):
            return 0
        if not re.search("[a-z]", A):
            return 0
        if not re.search("[A-Z]", A):
            return 0
        special_chars = "@#%&!$*()."
        for c in special_chars:
            if c in A:
                return 1
        return 0
 --------------------------------------------------------------    
A = ['S', 'c', 'a', 'l', 'e', 'r', '@', '1']
if '@'in A or '#'in A or '%'in A or '&'in A or '!'in A or '$'in A or '*' in A:
    if len(A) < 16 and len(A) > 7:
        u=0
        l=0
        d=0
        for i in A:
            if i.islower():
                l+=1
            elif i.isupper():
                u+=1
            elif i.isdigit():
                d+=1
        if u>0 and l>0 and d>0:
            print(1)

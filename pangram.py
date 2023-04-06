class Solution:
    # @param A : list of strings
    # @return an integer
    def solve(self, A):
        if len(set(list("".join(A).lower()))) == 26 : return 1
        else: return 0
-----------------------

A = ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"]
A = ''.join(A)
a='abcdefghijklmnopqrstuvwxyz'
for i in a:
  if i not in A:
    print(0)
  A=A.replace(i,'')
if len(A)==0:
    print(1)
else:
    print(0)

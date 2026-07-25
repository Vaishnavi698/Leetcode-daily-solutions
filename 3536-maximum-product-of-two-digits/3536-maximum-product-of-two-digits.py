#Ques
#ou are given a positive integer n.Return the maximum product of any two digits in n.Note: You may use the same digit twice if it appears more than once in n.

 
#Solution


class Solution:

    def maxProduct(self, n: int) -> int:
       
        digits = sorted([int(d) for d in str(n)])
        
       
        return digits[-1] * digits[-2]
        
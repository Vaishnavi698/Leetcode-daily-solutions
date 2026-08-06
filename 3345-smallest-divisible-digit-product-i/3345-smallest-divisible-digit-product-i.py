#Ques
#You are given two integers n and t. Return the smallest number greater than or equal to n such that the product of its digits is divisible by t.


#Solution

class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        curr = n
        
        while True:
        
            prod = 1
            for digit in str(curr):
                prod *= int(digit)
                
          
            if prod % t == 0:
                return curr
                
            curr += 1
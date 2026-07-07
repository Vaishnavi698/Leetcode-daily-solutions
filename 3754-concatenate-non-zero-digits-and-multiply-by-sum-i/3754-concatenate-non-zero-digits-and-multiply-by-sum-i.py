#ques-
#You are given an integer n.Form a new integer x by concatenating all the non-zero digits of n in their original order. If there are no non-zero digits, x = 0.Let sum be the sum of digits in x.Return an integer representing the value of x * sum.

#Solution 

from typing import List

class Solution:
   
    def sumAndMultiply(self, n: int) -> int:
   
        str_n = str(n)
        
  
        non_zero_digits = [char for char in str_n if char != '0']
        
 
        if not non_zero_digits:
            return 0
            
    
        x = int("".join(non_zero_digits))
        
      
        digit_sum = sum(int(digit) for digit in non_zero_digits)
        
       
        return x * digit_sum
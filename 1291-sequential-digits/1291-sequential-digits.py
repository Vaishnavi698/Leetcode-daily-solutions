#Ques
#An integer has sequential digits if and only if each digit in the number is one more than the previous digit.Return a sorted list of all the integers in the range [low, high] inclusive that have sequential digits
        

#Solution

from typing import List

class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        sample = "123456789"
        ans = []
    
        for length in range(2, 10):
           
            for start in range(10 - length):
                substring = sample[start : start + length]
                num = int(substring)
                
               
                if low <= num <= high:
                    ans.append(num)
                    
        return ans

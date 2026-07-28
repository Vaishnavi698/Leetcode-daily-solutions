#Ques
#You are given a palindromic string s.Return the lexicographically smallest palindromic permutation of s.


#Solution

class Solution:
    def smallestPalindrome(self, s: str) -> str:
        n = len(s)
        half_len = n // 2
        
       
        first_half = sorted(s[:half_len])
        
        
        mid = s[half_len] if n % 2 != 0 else ""
        
      
        left_str = "".join(first_half)
        right_str = left_str[::-1]
        
        return left_str + mid + right_str
#Ques
#Given a string s, return the lexicographically smallest subsequence of s that contains all the distinct characters of s exactly once.

 #Solution


class Solution:
    def smallestSubsequence(self, s: str) -> str:
   
        last_occ = {char: i for i, char in enumerate(s)}
        
        stack = []
        seen = set()
        
        for i, char in enumerate(s):
         
            if char in seen:
                continue
                
       
            while stack and stack[-1] > char and last_occ[stack[-1]] > i:
                removed_char = stack.pop()
                seen.remove(removed_char)
                
            stack.append(char)
            seen.add(char)
            
        return "".join(stack)
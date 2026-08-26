#Ques
#You are given a binary string s and a positive integer k.A substring of s is beautiful if the number of 1's in it is exactly k.Let len be the length of the shortest beautiful substring.Return the lexicographically smallest beautiful substring of string s with length equal to len. If s doesn't contain a beautiful substring, return an empty string.A string a is lexicographically larger than a string b (of the same length) if in the first position where a and b differ, a has a character strictly larger than the corresponding character in b.For example, "abcd" is lexicographically larger than "abcc" because the first position they differ is at the fourth character, and d is greater than c.
 
 #Solution

class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        ones = [i for i, char in enumerate(s) if char == '1']
        
        if len(ones) < k:
            return ""
        
        res = ""
        
        for i in range(len(ones) - k + 1):
            start = ones[i]
            end = ones[i + k - 1]
            sub = s[start : end + 1]
            
            if not res or len(sub) < len(res) or (len(sub) == len(res) and sub < res):
                res = sub
                
        return res
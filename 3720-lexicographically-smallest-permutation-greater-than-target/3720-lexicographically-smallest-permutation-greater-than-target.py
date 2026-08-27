#Ques
#You are given two strings s and target, both having length n, consisting of lowercase English letters.Return the lexicographically smallest permutation of s that is strictly greater than target. If no permutation of s is lexicographically strictly greater than target, return an empty string.A string a is lexicographically strictly greater than a string b (of the same length) if in the first position where a and b differ, string a has a letter that appears later in the alphabet than the corresponding letter in b.

#Solution

from collections import Counter

class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        n = len(s)
        count = Counter(s)
    
        matched_len = 0
        while matched_len < n and count[target[matched_len]] > 0:
            count[target[matched_len]] -= 1
            matched_len += 1
        
        for i in range(matched_len, -1, -1):
       
            if i < matched_len:
                count[target[i]] += 1
                
            if i < n:
              
                target_char = target[i]
                for char_code in range(ord(target_char) + 1, ord('z') + 1):
                    ch = chr(char_code)
                    if count[ch] > 0:
                      
                        res = list(target[:i]) + [ch]
                        count[ch] -= 1
                     
                        for remain_code in range(ord('a'), ord('z') + 1):
                            r_ch = chr(remain_code)
                            if count[r_ch] > 0:
                                res.extend([r_ch] * count[r_ch])
                                
                        return "".join(res)
                        
        return ""
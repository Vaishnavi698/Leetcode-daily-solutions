#Ques
#You are given two strings word1 and word2.A string x is called almost equal to y if you can change at most one character in x to make it identical to y.A sequence of indices seq is called valid if:The indices are sorted in ascending order.Concatenating the characters at these indices in word1 in the same order results in a string that is almost equal to word2.Return an array of size word2.length representing the lexicographically smallest valid sequence of indices. If no such sequence of indices exists, return an empty array.Note that the answer must represent the lexicographically smallest array, not the corresponding string formed by those indices.

 #Solution

class Solution:
    def validSequence(self, word1: str, word2: str) -> list[int]:
        n, m = len(word1), len(word2)
        
 
        last = [-1] * (m + 1)
        last[m] = n
        
        ptr = n - 1
        for i in range(m - 1, -1, -1):
            while ptr >= 0 and word1[ptr] != word2[i]:
                ptr -= 1
            last[i] = ptr
            if ptr >= 0:
                ptr -= 1
        
       
        ans = []
        w1_idx = 0
        changed = False
        
        for i in range(m):
            found = False
            while w1_idx < n:
                j = w1_idx
                is_match = (word1[j] == word2[i])
                
               
                if is_match:
                    if not changed or last[i + 1] > j:
                        ans.append(j)
                        w1_idx = j + 1
                        found = True
                        break
                else:
                    if not changed and last[i + 1] > j:
                        ans.append(j)
                        changed = True
                        w1_idx = j + 1
                        found = True
                        break
                
                w1_idx += 1
                
            if not found:
                return []
                
        return ans
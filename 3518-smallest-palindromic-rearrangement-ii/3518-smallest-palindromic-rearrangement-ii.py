#Ques
#You are given a palindromic string s and an integer k.Return the k-th lexicographically smallest palindromic permutation of s. If there are fewer than k distinct palindromic permutations, return an empty string.
#Note: Different rearrangements that yield the same palindromic string are considered identical and are counted once.

 
#Solution


from collections import Counter

class Solution:
    MAX = 10**6 + 1

    def smallestPalindrome(self, s: str, k: int) -> str:
        count = Counter(s)
        
      
        half_count = [0] * 26
        mid_letter = ''
        for c, freq in count.items():
            half_count[ord(c) - ord('a')] = freq // 2
            if freq % 2 == 1:
                mid_letter = c
                
      
        def nCk(n: int, r: int) -> int:
            if r < 0 or r > n:
                return 0
            res = 1
            for i in range(1, min(r, n - r) + 1):
                res = res * (n - i + 1) // i
                if res >= self.MAX:
                    return self.MAX
            return res

    
        def count_arrangements(counts: list) -> int:
            total = sum(counts)
            res = 1
            for freq in counts:
                if freq == 0:
                    continue
                res *= nCk(total, freq)
                if res >= self.MAX:
                    return self.MAX
                total -= freq
            return res

    
        total_perms = count_arrangements(half_count)
        if k > total_perms:
            return ""

        half_len = sum(half_count)
        left = []
        
        for _ in range(half_len):
            for i in range(26):
                if half_count[i] == 0:
                    continue
                
                half_count[i] -= 1
                arrangements = count_arrangements(half_count)
                
                if arrangements >= k:
                    left.append(chr(i + ord('a')))
                    break
                else:
                    k -= arrangements
                    half_count[i] += 1
                    
        left_str = "".join(left)
        return left_str + mid_letter + left_str[::-1]
class Solution:
    def distinctSubseqII(self, s: str) -> int:
        MOD = 10**9 + 7
        # Stores the count of distinct subsequences ending at each character
        last = [0] * 26
        
        for char in s:
            idx = ord(char) - ord('a')
            # New subsequences created by appending `char` to all existing ones + 1 (the char itself)
            last[idx] = (sum(last) + 1) % MOD
            
        return sum(last) % MOD
#Ques
#You are given a binary string s of length n, where:
#'1' represents an active section.
#'0' represents an inactive section.
#You can perform at most one trade to maximize the number of active sections in s. In a trade, you:Convert a contiguous block of '1's that is surrounded by '0's to all '0's.Afterward, convert a contiguous block of '0's that is surrounded by '1's to all '1's.Return the maximum number of active sections in s after making the optimal trade.


#Solution


class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        total_ones = s.count('1')
    
        zero_blocks = []
        cur_zeros = 0
        
        for char in s:
            if char == '0':
                cur_zeros += 1
            else:
                if cur_zeros > 0:
                    zero_blocks.append(cur_zeros)
                    cur_zeros = 0
        if cur_zeros > 0:
            zero_blocks.append(cur_zeros)
            
       
        if len(zero_blocks) < 2:
            return total_ones
      
        max_gain = 0
        for i in range(len(zero_blocks) - 1):
            max_gain = max(max_gain, zero_blocks[i] + zero_blocks[i + 1])
            
        return total_ones + max_gain
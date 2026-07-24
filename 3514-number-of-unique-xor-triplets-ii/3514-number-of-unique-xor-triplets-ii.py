#Ques
#You are given an integer array nums.A XOR triplet is defined as the XOR of three elements nums[i] XOR nums[j] XOR nums[k] where i <= j <= k.Return the number of unique XOR triplet values from all possible triplets (i, j, k).


#Solution

class Solution:
    def uniqueXorTriplets(self, nums: list[int]) -> int:
        n = len(nums)
        
 
        max_val = max(nums)
        T = 1
        while T <= max_val:
            T <<= 1
        T <<= 1 
        
   
        s1 = [False] * T
        for i in range(n):
            for j in range(i, n):
                s1[nums[i] ^ nums[j]] = True
                
       
        s2 = [False] * T
        for v in range(T):
            if s1[v]:
                for num in nums:
                    s2[v ^ num] = True
                    
       
        return sum(s2)


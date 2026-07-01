class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
       
        seen_numbers = {}
        
      
        for i, num in enumerate(nums):
            
            needed_partner = target - num
            
           
            if needed_partner in seen_numbers:
                
                return [seen_numbers[needed_partner], i]
            
            
            seen_numbers[num] = i
            
        return []
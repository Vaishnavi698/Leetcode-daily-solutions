class Solution:
    def minimizeSum(self, nums: List[int]) -> int:
        nums.sort()
        
        # Option 1: Change the two smallest elements
        opt1 = nums[-1] - nums[2]
        
        # Option 2: Change the two largest elements
        opt2 = nums[-3] - nums[0]
        
        # Option 3: Change one smallest and one largest element
        opt3 = nums[-2] - nums[1]
        
        return min(opt1, opt2, opt3)

class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        # Check if the sum is out of valid bounds
        if sum < 1 or sum > 9 * num:
            return ""
        
        digits = []
        rem_sum = sum
        
        for i in range(num):
            # Take the largest possible digit for the current position
            d = min(9, rem_sum)
            digits.append(str(d))
            rem_sum -= d
            
        return "".join(digits)
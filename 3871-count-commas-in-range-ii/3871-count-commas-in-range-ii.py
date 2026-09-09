class Solution:
    def countCommas(self, n: int) -> int:
        total_commas = 0
        threshold = 1000
        
        while n >= threshold:
            # Count how many numbers in [1, n] are >= threshold
            total_commas += n - threshold + 1
            threshold *= 1000
            
        return total_commas
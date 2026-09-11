from collections import Counter
from typing import List

class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        available_counts = Counter(digits)
        valid_count = 0
        
        # Check all 3-digit even numbers
        for num in range(100, 1000, 2):
            d1 = num // 100
            d2 = (num // 10) % 10
            d3 = num % 10
            
            num_counts = Counter([d1, d2, d3])
            
            # Check if all required digits are available in digits array
            if all(available_counts[d] >= count for d, count in num_counts.items()):
                valid_count += 1
                
        return valid_count
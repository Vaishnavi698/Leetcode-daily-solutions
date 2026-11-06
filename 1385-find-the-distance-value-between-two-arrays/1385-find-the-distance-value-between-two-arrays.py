from typing import List
import bisect

class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        arr2.sort()
        distance_value = 0
        
        for x in arr1:
            # Find the insertion point for x in arr2
            idx = bisect.bisect_left(arr2, x)
            
            # Check the closest element to the left
            valid = True
            if idx > 0 and abs(arr2[idx - 1] - x) <= d:
                valid = False
            # Check the closest element to the right
            if idx < len(arr2) and abs(arr2[idx] - x) <= d:
                valid = False
                
            if valid:
                distance_value += 1
                
        return distance_value
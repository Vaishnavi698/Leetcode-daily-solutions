from typing import List

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        n = len(nums)
        counts = [0] * n
        # Pair each element with its initial index: (value, index)
        enum_nums = list(enumerate(nums))
        
        def merge_sort(enum_arr):
            half = len(enum_arr) // 2
            if half:
                left, right = merge_sort(enum_arr[:half]), merge_sort(enum_arr[half:])
                
                merged = []
                i = j = 0
                
                while i < len(left) and j < len(right):
                    # Compare original values: left[i][1] vs right[j][1]
                    if left[i][1] <= right[j][1]:
                        # Elements in right[:j] are all smaller than left[i]
                        counts[left[i][0]] += j
                        merged.append(left[i])
                        i += 1
                    else:
                        merged.append(right[j])
                        j += 1
                
                # Remaining elements in left half
                while i < len(left):
                    counts[left[i][0]] += j
                    merged.append(left[i])
                    i += 1
                    
                # Remaining elements in right half
                while j < len(right):
                    merged.append(right[j])
                    j += 1
                    
                return merged
            return enum_arr

        merge_sort(enum_nums)
        return counts
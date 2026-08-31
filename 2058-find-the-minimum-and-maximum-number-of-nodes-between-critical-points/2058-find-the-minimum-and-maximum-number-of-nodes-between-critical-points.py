from typing import List, Optional

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        if not head or not head.next or not head.next.next:
            return [-1, -1]
        
        prev = head
        curr = head.next
        index = 1
        
        first_critical = -1
        last_critical = -1
        min_dist = float('inf')
        
        while curr.next:
       
            is_maxima = curr.val > prev.val and curr.val > curr.next.val
            is_minima = curr.val < prev.val and curr.val < curr.next.val
            
            if is_maxima or is_minima:
                if first_critical == -1:
                    first_critical = index
                else:
                    min_dist = min(min_dist, index - last_critical)
                
                last_critical = index
                
            prev = curr
            curr = curr.next
            index += 1
            
       
        if first_critical == last_critical or first_critical == -1:
            return [-1, -1]
            
        max_dist = last_critical - first_critical
        return [min_dist, max_dist]
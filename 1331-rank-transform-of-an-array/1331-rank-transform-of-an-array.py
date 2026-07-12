#Ques
#Given an array of integers arr, replace each element with its rank.The rank represents how large the element is. The rank has the following rules:Rank is an integer starting from 1.The larger the element, the larger the rank. If two elements are equal, their rank must be the same.Rank should be as small as possible.
 


#Solution

from typing import List

class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:

        sorted_unique = sorted(list(set(arr)))
        
       
        rank_map = {val: rank for rank, val in enumerate(sorted_unique, 1)}
  
        return [rank_map[num] for num in arr]
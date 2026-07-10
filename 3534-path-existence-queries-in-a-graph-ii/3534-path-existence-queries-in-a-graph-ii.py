#Ques 
#You are given an integer n representing the number of nodes in a graph, labeled from 0 to n - 1.You are also given an integer array nums of length n and an integer maxDiff.An undirected edge exists between nodes i and j if the absolute difference between nums[i] and nums[j] is at most maxDiff (i.e., |nums[i] - nums[j]| <= maxDiff).You are also given a 2D integer array queries. For each queries[i] = [ui, vi], find the minimum distance between nodes ui and vi. If no path exists between the two nodes, return -1 for that query.Return an array answer, where answer[i] is the result of the ith query.Note: The edges between the nodes are unweighted.

 #Solution

import bisect
from typing import List

class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[int]:
      
        unique_vals = sorted(list(set(nums)))
        m = len(unique_vals)
        
       
        next_far = [0] * m
        for i in range(m):
            limit = unique_vals[i] + maxDiff
          
            idx = bisect.bisect_right(unique_vals, limit) - 1
            next_far[i] = idx
            
      
        LOG = 18 
        up = [[0] * m for _ in range(LOG)]
        
        for i in range(m):
            up[0][i] = next_far[i]
            
        for j in range(1, LOG):
            for i in range(m):
                up[j][i] = up[j - 1][up[j - 1][i]]
                
        
        ans = []
        for u, v in queries:
            if u == v:
                ans.append(0)
                continue
                
            val_u = nums[u]
            val_v = nums[v]
            
            if val_u == val_v:
                ans.append(1)
                continue
                
          
            x_val, y_val = min(val_u, val_v), max(val_u, val_v)
            
            idx_x = bisect.bisect_left(unique_vals, x_val)
            idx_y = bisect.bisect_left(unique_vals, y_val)
            
         
            curr = idx_x
            for j in range(LOG - 1, -1, -1):
                curr = up[j][curr]
            if curr < idx_y:
                ans.append(-1)
                continue
                
          
            steps = 0
            curr = idx_x
            for j in range(LOG - 1, -1, -1):
                if up[j][curr] < idx_y:
                    curr = up[j][curr]
                    steps += (1 << j)
           
            steps += 1
            ans.append(steps)
            
        return ans
        
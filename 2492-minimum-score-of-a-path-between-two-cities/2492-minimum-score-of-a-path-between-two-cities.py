#Ques

#You are given a positive integer n representing n cities numbered from 1 to n. You are also given a 2D array roads where roads[i] = [ai, bi, distancei] indicates that there is a bidirectional road between cities ai and bi with a distance equal to distancei. The cities graph is not necessarily connected.
#The score of a path between two cities is defined as the minimum distance of a road in this path.
#Return the minimum possible score of a path between cities 1 and n.



#Solution

from collections import deque
from typing import List

class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
       
        graph = [[] for _ in range(n + 1)]
        for u, v, dist in roads:
            graph[u].append((v, dist))
            graph[v].append((u, dist))  
            
      
        queue = deque([1])
        visited = set([1])
        
      
        min_score = float('inf')
        
        while queue:
            curr_city = queue.popleft()
            
           
            for neighbor, dist in graph[curr_city]:
              
                min_score = min(min_score, dist)
                
               
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
                    
        return min_score
        
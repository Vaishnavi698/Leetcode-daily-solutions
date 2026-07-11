#Ques
#You are given an integer n. There is an undirected graph with n vertices, numbered from 0 to n - 1. You are given a 2D integer array edges where edges[i] = [ai, bi] denotes that there exists an undirected edge connecting vertices ai and bi.Return the number of complete connected components of the graph.A connected component is a subgraph of a graph in which there exists a path between any two vertices, and no vertex of the subgraph shares an edge with a vertex outside of the subgraph.A connected component is said to be complete if there exists an edge between every pair of its vertices.


#Solution

from typing import List
from collections import deque

class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
      
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            
        visited = [False] * n
        complete_components_count = 0
        
       
        for i in range(n):
            if not visited[i]:
             
                queue = deque([i])
                visited[i] = True
                
                vertex_count = 0
                edge_count = 0
                
                while queue:
                    curr = queue.popleft()
                    vertex_count += 1
                  
                    edge_count += len(adj[curr])
                    
                    for neighbor in adj[curr]:
                        if not visited[neighbor]:
                            visited[neighbor] = True
                            queue.append(neighbor)
                
             
                if edge_count == vertex_count * (vertex_count - 1):
                    complete_components_count += 1
                    
        return complete_components_count
        
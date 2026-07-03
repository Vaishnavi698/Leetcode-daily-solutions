#QUESTION:-
#You are given a directed acyclic graph of n nodes numbered from 0 to n − 1. This is represented by a 2D array edges of length m, where edges[i] = [ui, vi, costi] indicates a one‑way communication from node ui to node vi with a recovery cost of costi.

#Some nodes may be offline. You are given a boolean array online where online[i] = true means node i is online. Nodes 0 and n − 1 are always online.

#A path from 0 to n − 1 is valid if:

#All intermediate nodes on the path are online.
#The total recovery cost of all edges on the path does not exceed k.
#For each valid path, define its score as the minimum edge‑cost along that path.

#return the maximum path score (i.e., the largest minimum-edge cost) among all valid paths. If no valid path exists, return -1.

#sOLUTION 


import heapq
from typing import List

class Solution:
    def findMaxPathScore(self, edges: List[List[int]], online: List[bool], k: int) -> int:
        n = len(online)
        
        # Step 1: Build the Adjacency List
        graph = [[] for _ in range(n)]
        unique_costs = set()
        
        for u, v, cost in edges:
            graph[u].append((v, cost))
            unique_costs.add(cost)
            
        # Sort unique costs to prepare for our Binary Search game
        costs_list = sorted(list(unique_costs))
        
        # Step 2: Reliable Dijkstra path checking
        def can_reach(min_allowed_toll: int) -> bool:
            # If the starting point or destination point is offline, it's impossible
            if not online[0] or not online[n - 1]:
                return False
                
            # Distances array initialized to infinity
            distances = [float('inf')] * n
            distances[0] = 0
            
            # Min-Priority Queue stores tuples of: (accumulated_cost, current_node)
            pq = [(0, 0)]
            
            while pq:
                curr_cost, u = heapq.heappop(pq)
                
                # If we found a more expensive path to an already processed node, skip it
                if curr_cost > distances[u]:
                    continue
                    
                # If we reached the destination within our budget, this bottleneck value works!
                if u == n - 1:
                    return curr_cost <= k
                    
                for v, cost in graph[u]:
                    # Filter out roads that are lower than our binary search target bottle-neck
                    if cost < min_allowed_toll:
                        continue
                    # Skip offline nodes
                    if not online[v]:
                        continue
                        
                    next_cost = curr_cost + cost
                    # Optimization: only traverse if it's cheaper than what we found before and stays under budget
                    if next_cost < distances[v] and next_cost <= k:
                        distances[v] = next_cost
                        heapq.heappush(pq, (next_cost, v))
                        
            return distances[n - 1] <= k

        # Step 3: Binary Search over the sorted list of unique toll costs
        low = 0
        high = len(costs_list) - 1
        ans = -1
        
        while low <= high:
            mid = (low + high) // 2
            guess_toll = costs_list[mid]
            
            if can_reach(guess_toll):
                ans = guess_toll  # Valid path found! Save this guess
                low = mid + 1     # Push the boundary higher to maximize the minimum edge
            else:
                high = mid - 1    # Too restrictive, look for cheaper minimums
                
        return ans
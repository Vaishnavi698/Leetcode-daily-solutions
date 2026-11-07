from typing import List
import heapq

class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        n = len(servers)
        m = len(tasks)
        
        # Available servers min-heap: stores (weight, index)
        available = []
        for i, weight in enumerate(servers):
            heapq.heappush(available, (weight, i))
            
        # Busy servers min-heap: stores (free_time, weight, index)
        busy = []
        
        ans = [0] * m
        current_time = 0
        
        for j in range(m):
            # Advance time to the current task's arrival time, or at least keep it moving
            current_time = max(current_time, j)
            
            # Free up servers whose task completion time <= current_time
            while busy and busy[0][0] <= current_time:
                free_time, weight, idx = heapq.heappop(busy)
                heapq.heappush(available, (weight, idx))
                
            # If no servers are available, jump time to when the next busy server becomes free
            if not available:
                current_time = busy[0][0]
                while busy and busy[0][0] <= current_time:
                    free_time, weight, idx = heapq.heappop(busy)
                    heapq.heappush(available, (weight, idx))
                    
            # Assign the task to the best available server
            weight, idx = heapq.heappop(available)
            ans[j] = idx
            
            # Push the server into the busy heap with its new completion time
            completion_time = current_time + tasks[j]
            heapq.heappush(busy, (completion_time, weight, idx))
            
        return ans
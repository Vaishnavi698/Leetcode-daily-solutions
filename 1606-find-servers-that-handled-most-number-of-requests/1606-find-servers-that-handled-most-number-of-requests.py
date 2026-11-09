from typing import List
import heapq
from sortedcontainers import SortedList

class Solution:
    def busiestServers(self, k: int, arrival: List[int], load: List[int]) -> List[int]:
        # Min-heap to store busy servers: (free_time, server_id)
        busy = []
        
        # SortedList to keep track of available server IDs
        available = SortedList(range(k))
        
        request_count = [0] * k
        
        for i in range(n := len(arrival)):
            curr_time = arrival[i]
            duration = load[i]
            
            # 1. Free up servers whose tasks have finished by curr_time
            while busy and busy[0][0] <= curr_time:
                _, server_id = heapq.heappop(busy)
                available.add(server_id)
                
            # 2. If no servers are available, drop the request
            if not available:
                continue
                
            # 3. Find the next available server starting from (i % k)
            preferred = i % k
            idx = available.bisect_left(preferred)
            
            # If no available server >= preferred, wrap around to the beginning
            if idx == len(available):
                idx = 0
                
            server_id = available[idx]
            
            # 4. Assign the request to this server
            available.remove(server_id)
            request_count[server_id] += 1
            heapq.heappush(busy, (curr_time + duration, server_id))
            
        # 5. Find the maximum requests handled and return all servers matching that count
        max_requests = max(request_count)
        return [i for i, count in enumerate(request_count) if count == max_requests]
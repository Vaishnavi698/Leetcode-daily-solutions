from typing import List

class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        # Sort logs by timestamp
        logs.sort(key=lambda l: l[1])
        
        # Sort queries along with their original indices
        indexed_queries = sorted(enumerate(queries), key=lambda q: q[1])
        
        res = [0] * len(queries)
        server_counts = [0] * (n + 1)
        active_servers = 0
        
        log_idx = 0
        num_logs = len(logs)
        
        left = 0
        right = 0
        
        for orig_idx, q in indexed_queries:
            window_start = q - x
            window_end = q
            
            # Add logs whose timestamps are <= window_end
            while right < num_logs and logs[right][1] <= window_end:
                server_id = logs[right][0]
                if server_counts[server_id] == 0:
                    active_servers += 1
                server_counts[server_id] += 1
                right += 1
                
            # Remove logs whose timestamps are < window_start
            while left < num_logs and logs[left][1] < window_start:
                server_id = logs[left][0]
                server_counts[server_id] -= 1
                if server_counts[server_id] == 0:
                    active_servers -= 1
                left += 1
                
            # Zero-request servers = total servers - active servers
            res[orig_idx] = n - active_servers
            
        return res
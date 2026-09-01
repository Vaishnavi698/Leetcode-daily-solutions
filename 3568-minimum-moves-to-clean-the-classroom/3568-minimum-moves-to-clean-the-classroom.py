#Solution

from collections import deque
from typing import List

class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        m, n = len(classroom), len(classroom[0])
        
        start_r, start_c = -1, -1
        litter_positions = []
       
        for r in range(m):
            for c in range(n):
                ch = classroom[r][c]
                if ch == 'S':
                    start_r, start_c = r, c
                elif ch == 'L':
                    litter_positions.append((r, c))
                    
        total_litter = len(litter_positions)
        target_mask = (1 << total_litter) - 1
        
       
        litter_map = {pos: i for i, pos in enumerate(litter_positions)}
        
       
        initial_mask = 0
        if (start_r, start_c) in litter_map:
            initial_mask |= (1 << litter_map[(start_r, start_c)])
            
        
        if initial_mask == target_mask:
            return 0

        
        queue = deque([(start_r, start_c, initial_mask, energy)])
        
       
        max_energy_seen = {}
        max_energy_seen[(start_r, start_c, initial_mask)] = energy
        
        moves = 0
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        while queue:
            for _ in range(len(queue)):
                r, c, mask, curr_e = queue.popleft()
                
                if mask == target_mask:
                    return moves
                
            
                if curr_e == 0:
                    continue
                
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    
                 
                    if 0 <= nr < m and 0 <= nc < n and classroom[nr][nc] != 'X':
                        next_e = curr_e - 1
                        cell_type = classroom[nr][nc]
                        
                        
                        if cell_type == 'R':
                            next_e = energy
                            
                        next_mask = mask
                        
                        if cell_type == 'L' and (nr, nc) in litter_map:
                            next_mask |= (1 << litter_map[(nr, nc)])
                            
                        
                        if next_mask == target_mask:
                            return moves + 1
                            
                        state = (nr, nc, next_mask)
                        if next_e > max_energy_seen.get(state, -1):
                            max_energy_seen[state] = next_e
                            queue.append((nr, nc, next_mask, next_e))
                            
            moves += 1
            
        return -1
#Ques
#You are maintaining a project that has n methods numbered from 0 to n - 1.You are given two integers n and k, and a 2D integer array invocations, where invocations[i] = [ai, bi] indicates that method ai invokes method bi.There is a known bug in method k. Method k, along with any method invoked by it, either directly or indirectly, are considered suspicious and we aim to remove them.A group of methods can only be removed if no method outside the group invokes any methods within it.Return an array containing all the remaining methods after removing all the suspicious methods. You may return the answer in any order. If it is not possible to remove all the suspicious methods, none should be removed.

#Solution


from collections import defaultdict, deque
from typing import List

class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
       
        graph = defaultdict(list)
        for u, v in invocations:
            graph[u].append(v)
            
 
        suspicious = set([k])
        queue = deque([k])
        
        while queue:
            curr = queue.popleft()
            for neighbor in graph[curr]:
                if neighbor not in suspicious:
                    suspicious.add(neighbor)
                    queue.append(neighbor)
                    
       
        for u, v in invocations:
            if v in suspicious and u not in suspicious:
              
                return list(range(n))
                
      
        return [i for i in range(n) if i not in suspicious]
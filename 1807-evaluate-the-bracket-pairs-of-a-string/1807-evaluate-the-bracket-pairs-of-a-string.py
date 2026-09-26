from typing import List

class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        # Convert knowledge array to a hash map for O(1) lookup
        knowledge_map = {k: v for k, v in knowledge}
        
        res = []
        in_bracket = False
        current_key = []
        
        for char in s:
            if char == '(':
                in_bracket = True
            elif char == ')':
                in_bracket = False
                key_str = "".join(current_key)
                # Look up key in map, fallback to '?' if not present
                res.append(knowledge_map.get(key_str, '?'))
                current_key = []
            elif in_bracket:
                current_key.append(char)
            else:
                res.append(char)
                
        return "".join(res)
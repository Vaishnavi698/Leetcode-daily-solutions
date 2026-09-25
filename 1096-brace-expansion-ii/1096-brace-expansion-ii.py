from typing import List
import itertools

class Solution:
    def braceExpansionII(self, expression: str) -> List[str]:
        # Stack maintains tuples: (groups_accumulated, current_group)
        # groups_accumulated: list of sets separated by commas ','
        # current_group: set of strings accumulated via concatenation
        stack = []
        groups = []
        cur_group = {""}

        for char in expression:
            if char.isalpha():
                # Concatenate letter to all strings in the current group
                cur_group = {word + char for word in cur_group}
            elif char == '{':
                # Push current scope state onto stack and start a fresh scope
                stack.append((groups, cur_group))
                groups, cur_group = [], {""}
            elif char == ',':
                # Comma ends the current group and adds it to current scope's groups
                groups.append(cur_group)
                cur_group = {""}
            elif char == '}':
                # Close current scope by taking union of all comma groups
                groups.append(cur_group)
                union_set = set().union(*groups)
                
                # Restore parent scope from stack
                prev_groups, prev_cur_group = stack.pop()
                
                # Multiply parent's current_group with the evaluated union_set
                cur_group = {a + b for a in prev_cur_group for b in union_set}
                groups = prev_groups

        # Add remaining group to groups list and take union
        groups.append(cur_group)
        final_set = set().union(*groups)
        
        return sorted(list(final_set))
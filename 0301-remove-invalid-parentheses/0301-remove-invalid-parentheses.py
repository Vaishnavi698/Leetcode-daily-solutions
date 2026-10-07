from collections import deque

class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        def is_valid(string: str) -> bool:
            balance = 0
            for char in string:
                if char == '(':
                    balance += 1
                elif char == ')':
                    balance -= 1
                    if balance < 0:
                        return False
            return balance == 0

        result = []
        visited = {s}
        queue = deque([s])
        found = False

        while queue:
            curr = queue.popleft()

            if is_valid(curr):
                result.append(curr)
                found = True

            # If we already found valid strings at this removal level, 
            # don't generate the next level of shorter strings
            if found:
                continue

            # Generate all possible states by removing one parenthesis
            for i in range(len(curr)):
                if curr[i] not in ('(', ')'):
                    continue
                
                # Skip consecutive duplicate characters to prune search space
                if i > 0 and curr[i] == curr[i - 1]:
                    continue

                next_str = curr[:i] + curr[i+1:]
                if next_str not in visited:
                    visited.add(next_str)
                    queue.append(next_str)

        return result
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracket_map = {')': '(', '}': '{', ']': '['}
        
        for char in s:
            if char in bracket_map:
                # Pop top element if stack is not empty, else assign dummy value
                top_element = stack.pop() if stack else '#'
                
                # If mapped opening bracket doesn't match top element, string is invalid
                if bracket_map[char] != top_element:
                    return False
            else:
                # Open bracket -> push to stack
                stack.append(char)
                
        # Valid if all opening brackets were closed
        return len(stack) == 0
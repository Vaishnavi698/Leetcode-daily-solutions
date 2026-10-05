class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        score = 0
        depth = 0
        
        for i in range(len(s)):
            if s[i] == '(':
                depth += 1
            else:
                depth -= 1
                # Check if this ')' forms a core pair '()'
                if s[i - 1] == '(':
                    score += 1 << depth  # Equivalent to 2^depth
                    
        return score
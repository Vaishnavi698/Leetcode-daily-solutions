class Solution:
    def checkValidString(self, s: str) -> bool:
        min_open = 0
        max_open = 0
        
        for char in s:
            if char == '(':
                min_open += 1
                max_open += 1
            elif char == ')':
                min_open -= 1
                max_open -= 1
            else:  # char == '*'
                min_open -= 1  # '*' treated as ')'
                max_open += 1  # '*' treated as '('
            
            # If max_open is negative, we have more ')' than possible '(' and '*'
            if max_open < 0:
                return False
            
            # min_open cannot be negative; reset to 0
            min_open = max(0, min_open)
            
        return min_open == 0
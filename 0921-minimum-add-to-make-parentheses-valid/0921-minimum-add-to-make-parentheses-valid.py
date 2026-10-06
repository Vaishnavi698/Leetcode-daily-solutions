class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        open_needed = 0  # Unmatched ')' requiring '('
        balance = 0      # Unmatched '(' requiring ')'
        
        for char in s:
            if char == '(':
                balance += 1
            else:  # char == ')'
                if balance > 0:
                    balance -= 1
                else:
                    open_needed += 1
                    
        return open_needed + balance
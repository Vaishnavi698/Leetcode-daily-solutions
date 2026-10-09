class Solution:
    def minInsertions(self, s: str) -> int:
        insertions = 0
        open_count = 0
        i = 0
        n = len(s)
        
        while i < n:
            if s[i] == '(':
                open_count += 1
                i += 1
            else:  # s[i] == ')'
                # Check if there is a consecutive ')'
                if i + 1 < n and s[i + 1] == ')':
                    i += 2  # Consumed "))"
                else:
                    insertions += 1  # Missing a ')', so insert 1
                    i += 1  # Consumed single ')'
                
                # Balance against available '('
                if open_count > 0:
                    open_count -= 1
                else:
                    insertions += 1  # Missing a '(', so insert 1
                    
        # Any remaining unclosed '(' need two ')' each
        insertions += open_count * 2
        return insertions
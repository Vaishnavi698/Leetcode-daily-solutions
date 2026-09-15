class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        n = len(s)
        ans = 0
        last_end = -1  # Tracks the end index of the last chosen non-overlapping palindrome
        
        # Helper function to expand around center
        def expand_and_check(left: int, right: int):
            nonlocal ans, last_end
            while left >= 0 and right < n and s[left] == s[right]:
                length = right - left + 1
                # Check if this palindrome comes strictly after the previous match
                if length >= k:
                    if left > last_end:
                        ans += 1
                        last_end = right
                    break  # Greedily stop expansion for this center once valid length is reached
                left -= 1
                right += 1

        for i in range(n):
            # Check odd-length palindromes (single-character center)
            expand_and_check(i, i)
            # Check even-length palindromes (two-character center)
            expand_and_check(i, i + 1)
            
        return ans
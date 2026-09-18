from typing import List

class Solution:
    def maxNumOfSubstrings(self, s: str) -> List[str]:
        # Track first and last occurrences of each character
        first = {}
        last = {}
        for i, char in enumerate(s):
            if char not in first:
                first[char] = i
            last[char] = i

        valid_intervals = []

        # Find all valid self-contained intervals
        for char, l in first.items():
            r = last[char]
            valid = True
            curr = l
            
            while curr <= r:
                c = s[curr]
                # If a character's first occurrence is before l, l is invalid
                if first[c] < l:
                    valid = False
                    break
                # Expand right boundary to encompass all occurrences of c
                r = max(r, last[c])
                curr += 1

            if valid:
                valid_intervals.append((l, r))

        # Sort intervals by ending index for greedy selection
        valid_intervals.sort(key=lambda x: x[1])

        ans = []
        last_end = -1

        for l, r in valid_intervals:
            if l > last_end:
                ans.append(s[l : r + 1])
                last_end = r

        return ans
class Solution:
    def reverseDegree(self, s: str) -> int:
        total = 0
        for i, char in enumerate(s, start=1):
            reversed_pos = 26 - (ord(char) - ord('a'))
            total += reversed_pos * i
        return total
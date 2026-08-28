#Ques
#You are given two strings s and target, each of length n, consisting of lowercase English letters.Return the lexicographically smallest string that is both a palindromic permutation of s and strictly greater than target. If no such permutation exists, return an empty string.

#Solution

from collections import Counter

class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        n = len(s)
        counts = Counter(s)
        
     
        odd_chars = [ch for ch, cnt in counts.items() if cnt % 2 != 0]
        if len(odd_chars) > 1:
            return ""
        
        mid_char = odd_chars[0] if odd_chars else ""
        half_counts = {ch: cnt // 2 for ch, cnt in counts.items()}
        
        m = n // 2
        
        def build_palindrome(half_prefix: list) -> str:
            first_half = "".join(half_prefix)
            second_half = first_half[::-1]
            if n % 2 == 1:
                return first_half + mid_char + second_half
            return first_half + second_half

        best = None

        def check_and_update(p_str: str):
            nonlocal best
            if p_str > target:
                if best is None or p_str < best:
                    best = p_str

        curr_half = []
        rem = half_counts.copy()
        matched = True
        
        for i in range(m):
            ch = target[i]
            if rem.get(ch, 0) > 0:
                curr_half.append(ch)
                rem[ch] -= 1
            else:
                matched = False
                break
                
        if matched:
            check_and_update(build_palindrome(curr_half))
 
        prefix = []
        rem = half_counts.copy()
        
        for i in range(m):
            target_ch = target[i]
            for c_code in range(ord(target_ch) + 1, ord('z') + 1):
                ch = chr(c_code)
                if rem.get(ch, 0) > 0:
                    temp_half = prefix + [ch]
                    temp_rem = rem.copy()
                    temp_rem[ch] -= 1
                    
                    for code in range(ord('a'), ord('z') + 1):
                        fill_ch = chr(code)
                        if temp_rem.get(fill_ch, 0) > 0:
                            temp_half.extend([fill_ch] * temp_rem[fill_ch])
                            
                    check_and_update(build_palindrome(temp_half))

            if rem.get(target_ch, 0) > 0:
                prefix.append(target_ch)
                rem[target_ch] -= 1
            else:
                break

        return best if best is not None else ""
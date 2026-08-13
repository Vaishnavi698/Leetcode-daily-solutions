#Ques
#You are given a 0-indexed string s. You are also given a 0-indexed string queryCharacters of length k and a 0-indexed array of integer indices queryIndices of length k, both of which are used to describe k queries.The ith query updates the character in s at index queryIndices[i] to the character queryCharacters[i].Return an array lengths of length k where lengths[i] is the length of the longest substring of s consisting of only one repeating character after the ith query is performed.


#Solution

class Solution:
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: list[int]) -> list[int]:
        n = len(s)
        
       
        max_len = [0] * (4 * n)
        pref_len = [0] * (4 * n)
        suff_len = [0] * (4 * n)
        pref_char = [''] * (4 * n)
        suff_char = [''] * (4 * n)

        def merge(node, l_node, r_node, l_size, r_size):
         
            pref_char[node] = pref_char[l_node]
            pref_len[node] = pref_len[l_node]
            if pref_len[l_node] == l_size and pref_char[l_node] == pref_char[r_node]:
                pref_len[node] = l_size + pref_len[r_node]

          
            suff_char[node] = suff_char[r_node]
            suff_len[node] = suff_len[r_node]
            if suff_len[r_node] == r_size and suff_char[r_node] == suff_char[l_node]:
                suff_len[node] = r_size + suff_len[l_node]

          
            max_len[node] = max(max_len[l_node], max_len[r_node])
            if suff_char[l_node] == pref_char[r_node]:
                max_len[node] = max(max_len[node], suff_len[l_node] + pref_len[r_node])

        def build(node, l, r):
            if l == r:
                max_len[node] = 1
                pref_len[node] = 1
                suff_len[node] = 1
                pref_char[node] = s[l]
                suff_char[node] = s[l]
                return
            
            mid = (l + r) // 2
            l_node, r_node = 2 * node, 2 * node + 1
            build(l_node, l, mid)
            build(r_node, mid + 1, r)
            merge(node, l_node, r_node, mid - l + 1, r - mid)

        def update(node, l, r, idx, ch):
            if l == r:
                pref_char[node] = ch
                suff_char[node] = ch
                return
            
            mid = (l + r) // 2
            l_node, r_node = 2 * node, 2 * node + 1
            if idx <= mid:
                update(l_node, l, mid, idx, ch)
            else:
                update(r_node, mid + 1, r, idx, ch)
            merge(node, l_node, r_node, mid - l + 1, r - mid)

      
        build(1, 0, n - 1)
        
        
        ans = []
        for ch, idx in zip(queryCharacters, queryIndices):
            update(1, 0, n - 1, idx, ch)
            ans.append(max_len[1])
            
        return ans
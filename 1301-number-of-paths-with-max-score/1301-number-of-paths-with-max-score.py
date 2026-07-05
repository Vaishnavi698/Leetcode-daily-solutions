#ques:-
#Number of paths with max score
#You are given a square board of characters. You can move on the board starting at the bottom right square marked with the character 'S'.

#You need to reach the top left square marked with the character 'E'. The rest of the squares are labeled either with a numeric character 1, 2, ..., 9 or with an obstacle 'X'. In one move you can go up, left or up-left (diagonally) only if there is no obstacle there.

#Return a list of two integers: the first integer is the maximum sum of numeric characters you can collect, and the second is the number of such paths that you can take to get that maximum sum, taken modulo 10^9 + 7.

#In case there is no path, return [0, 0].


#Solution


from typing import List

class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        n = len(board)
        MOD = 10**9 + 7
        
       
        dp = [[[0, 0] for _ in range(n)] for _ in range(n)]
        
        dp[n-1][n-1] = [0, 1]
        
        
        for r in range(n - 1, -1, -1):
            for c in range(n - 1, -1, -1):
               
                if board[r][c] == 'X' or (r == n - 1 and c == n - 1):
                    continue
                
                max_score = -1
                path_count = 0
                
               
                for dr, dc in [(0, 1), (1, 0), (1, 1)]:
                    prev_r, prev_c = r + dr, c + dc
                    
                  
                    if prev_r < n and prev_c < n:
                        prev_score, prev_paths = dp[prev_r][prev_c]
                        
                       
                        if prev_paths > 0:
                            if prev_score > max_score:
                                max_score = prev_score
                                path_count = prev_paths
                            elif prev_score == max_score:
                                path_count = (path_count + prev_paths) % MOD
                
               
                if max_score != -1:
             
                    current_val = int(board[r][c]) if board[r][c] != 'E' else 0
                    dp[r][c] = [max_score + current_val, path_count]
                    
       
        final_score, final_paths = dp[0][0]
        return [final_score, final_paths]
        
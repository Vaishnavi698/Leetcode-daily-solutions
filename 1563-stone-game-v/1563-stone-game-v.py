#Ques
#There are several stones arranged in a row, and each stone has an associated value which is an integer given in the array stoneValue.In each round of the game, Alice divides the row into two non-empty rows (i.e. left row and right row), then Bob calculates the value of each row which is the sum of the values of all the stones in this row. Bob throws away the row which has the maximum value, and Alice's score increases by the value of the remaining row. If the value of the two rows are equal, Bob lets Alice decide which row will be thrown away. The next round starts with the remaining row.The game ends when there is only one stone remaining. Alice's score is initially zero.Return the maximum score that Alice can obtain.

 #Solution

class Solution:
    def stoneGameV(self, stoneValue: list[int]) -> int:
        n = len(stoneValue)
      
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + stoneValue[i]
            
        dp = [[0] * n for _ in range(n)]
        left_max = [[0] * n for _ in range(n)]
        right_max = [[0] * n for _ in range(n)]
      
        for i in range(n - 1, -1, -1):
            dp[i][i] = 0
            left_max[i][i] = prefix[i + 1]
            right_max[i][i] = -prefix[i]
            
            k = i
            for j in range(i + 1, n):
         
                while k < j and 2 * prefix[k + 1] <= prefix[i] + prefix[j + 1]:
                    k += 1
                
                mid_k = k - 1
                res = 0
             
              
                if mid_k >= i:
                    res = max(res, left_max[i][mid_k] - prefix[i])
                
             
                start_right = mid_k + 1 if 2 * prefix[mid_k + 1] == prefix[i] + prefix[j + 1] else mid_k + 2
                if start_right <= j:
                    res = max(res, right_max[start_right][j] + prefix[j + 1])
                    
                dp[i][j] = res
                
              
                left_max[i][j] = max(left_max[i][j - 1], res + prefix[j + 1])
                right_max[i][j] = max(right_max[i + 1][j], res - prefix[i])
                
        return dp[0][n - 1]
#Ques
#Alice and Bob continue their games with piles of stones. There are several stones arranged in a row, and each stone has an associated value which is an integer given in the array stoneValue.Alice and Bob take turns, with Alice starting first. On each player's turn, that player can take 1, 2, or 3 stones from the first remaining stones in the row.The score of each player is the sum of the values of the stones taken. The score of each player is 0 initially.The objective of the game is to end with the highest score, and the winner is the player with the highest score and there could be a tie. The game continues until all the stones have been taken.Assume Alice and Bob play optimally.Return "Alice" if Alice will win, "Bob" if Bob will win, or "Tie" if they will end the game with the same score.

#Solution

class Solution:
    def stoneGameIII(self, stoneValue: list[int]) -> str:
        n = len(stoneValue)
      
        dp = [0, 0, 0]

        for i in range(n - 1, -1, -1):
            max_diff = float('-inf')
            take_sum = 0
            
            for k in range(1, 4):
                if i + k <= n:
                    take_sum += stoneValue[i + k - 1]
                    max_diff = max(max_diff, take_sum - dp[k - 1])
            
          
            dp = [max_diff, dp[0], dp[1]]

        if dp[0] > 0:
            return "Alice"
        elif dp[0] < 0:
            return "Bob"
        else:
            return "Tie"
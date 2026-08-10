#Ques

#Alice and Bob take turns playing a game, with Alice starting first.Initially, there are n stones in a pile. On each player's turn, that player makes a move consisting of removing any non-zero square number of stones in the pile.Also, if a player cannot make a move, he/she loses the game.Given a positive integer n, return true if and only if Alice wins the game otherwise return false, assuming both players play optimally.


#Solution

class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        dp = [False] * (n + 1)
        
        for i in range(1, n + 1):
            k = 1
            while k * k <= i:
              
                if not dp[i - k * k]:
                    dp[i] = True
                    break  
                k += 1
                
        return dp[n]
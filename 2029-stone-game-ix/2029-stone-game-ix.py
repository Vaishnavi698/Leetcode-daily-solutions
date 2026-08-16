#Ques
#Alice and Bob continue their games with stones. There is a row of n stones, and each stone has an associated value. You are given an integer array stones, where stones[i] is the value of the ith stone.Alice and Bob take turns, with Alice starting first. On each turn, the player may remove any stone from stones. The player who removes a stone loses if the sum of the values of all removed stones is divisible by 3. Bob will win automatically if there are no remaining stones (even if it is Alice's turn).Assuming both players play optimally, return true if Alice wins and false if Bob wins.

 #Solution


class Solution:
    def stoneGameIX(self, stones: list[int]) -> bool:
        c0 = c1 = c2 = 0
        for x in stones:
            rem = x % 3
            if rem == 0:
                c0 += 1
            elif rem == 1:
                c1 += 1
            else:
                c2 += 1
                
        if c0 % 2 == 0:
            return c1 >= 1 and c2 >= 1
        else:
            return abs(c1 - c2) > 2
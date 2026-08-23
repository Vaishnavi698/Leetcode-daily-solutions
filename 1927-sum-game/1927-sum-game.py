#Ques
#Alice and Bob take turns playing a game, with Alice starting first.You are given a string num of even length consisting of digits and '?' characters. On each turn, a player will do the following if there is still at least one '?' in num:Choose an index i where num[i] == '?'.Replace num[i] with any digit between '0' and '9'.The game ends when there are no more '?' characters in num.For Bob to win, the sum of the digits in the first half of num must be equal to the sum of the digits in the second half. For Alice to win, the sums must not be equal.For example, if the game ended with num = "243801", then Bob wins because 2+4+3 = 8+0+1. If the game ended with num = "243803", then Alice wins because 2+4+3 != 8+0+3.Assuming Alice and Bob play optimally, return true if Alice will win and false if Bob will win.


#Solutiom

class Solution:
    def sumGame(self, num: str) -> bool:
        n = len(num)
        half = n // 2
        
        sum_left = sum_right = 0
        q_left = q_right = 0
        
       
        for i in range(half):
            if num[i] == '?':
                q_left += 1
            else:
                sum_left += int(num[i])
                
        for i in range(half, n):
            if num[i] == '?':
                q_right += 1
            else:
                sum_right += int(num[i])
                
        sum_diff = sum_left - sum_right
        q_diff = q_left - q_right
        
       
        if q_diff % 2 != 0:
            return True
            
       
        return sum_diff + (q_diff // 2) * 9 != 0
#ques
#You are given a positive integer n. Determine whether n is divisible by the sum of the following two values:The digit sum of n (the sum of its digits).The digit product of n (the product of its digits).Return true if n is divisible by this sum; otherwise, return false.

#Solution

class Solution:
    def checkDivisibility(self, n: int) -> bool:
        digit_sum = 0
        digit_product = 1
        temp = n
        
        while temp > 0:
            digit = temp % 10
            digit_sum += digit
            digit_product *= digit
            temp //= 10
            
        total_sum = digit_sum + digit_product
        
        return n % total_sum == 0
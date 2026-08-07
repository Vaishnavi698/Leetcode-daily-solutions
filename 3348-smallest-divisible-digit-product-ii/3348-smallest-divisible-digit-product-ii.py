#Ques
#You are given a string num which represents a positive integer, and an integer t.A number is called zero-free if none of its digits are 0.Return a string representing the smallest zero-free number greater than or equal to num such that the product of its digits is divisible by t. If no such number exists, return "-1".


#Solution

class Solution:
    def smallestNumber(self, num: str, t: int) -> str:
      
        c2 = c3 = c5 = c7 = 0
        temp_t = t
        
        while temp_t % 2 == 0:
            c2 += 1
            temp_t //= 2
        while temp_t % 3 == 0:
            c3 += 1
            temp_t //= 3
        while temp_t % 5 == 0:
            c5 += 1
            temp_t //= 5
        while temp_t % 7 == 0:
            c7 += 1
            temp_t //= 7
            
       
        if temp_t > 1:
            return "-1"

      
        FACTORS = {
            '1': (0, 0, 0, 0),
            '2': (1, 0, 0, 0),
            '3': (0, 1, 0, 0),
            '4': (2, 0, 0, 0),
            '5': (0, 0, 1, 0),
            '6': (1, 1, 0, 0),
            '7': (0, 0, 0, 1),
            '8': (3, 0, 0, 0),
            '9': (0, 2, 0, 0),
        }

    
        def min_len(req2: int, req3: int, req5: int, req7: int) -> int:
            req2, req3, req5, req7 = max(0, req2), max(0, req3), max(0, req5), max(0, req7)
            cnt8, rem2 = req2 // 3, req2 % 3
            cnt9, rem3 = req3 // 2, req3 % 2
            
            extra = 0
            if rem2 == 1 and rem3 == 1:
                extra = 1
            elif rem2 == 2 and rem3 == 1:
                extra = 2
            elif rem2 == 1 and rem3 == 0:
                extra = 1
            elif rem2 == 2 and rem3 == 0:
                extra = 1
            elif rem2 == 0 and rem3 == 1:
                extra = 1
                
            return req7 + req5 + cnt8 + cnt9 + extra

        def get_min_suffix(req2: int, req3: int, req5: int, req7: int) -> str:
            req2, req3, req5, req7 = max(0, req2), max(0, req3), max(0, req5), max(0, req7)
            cnt8, rem2 = req2 // 3, req2 % 3
            cnt9, rem3 = req3 // 2, req3 % 2
            
            digits = ['7'] * req7 + ['5'] * req5 + ['8'] * cnt8 + ['9'] * cnt9
            
            if rem2 == 1 and rem3 == 1:
                digits.append('6')
            elif rem2 == 2 and rem3 == 1:
                digits.extend(['2', '6'])
            elif rem2 == 1 and rem3 == 0:
                digits.append('2')
            elif rem2 == 2 and rem3 == 0:
                digits.append('4')
            elif rem2 == 0 and rem3 == 1:
                digits.append('3')
                
            digits.sort()
            return "".join(digits)

        L = len(num)
        
        
        first_zero = num.find('0')
        if first_zero == -1:
            first_zero = L
            
       
        pref2 = [0] * (L + 1)
        pref3 = [0] * (L + 1)
        pref5 = [0] * (L + 1)
        pref7 = [0] * (L + 1)
        
        for i in range(L):
            if num[i] != '0':
                f2, f3, f5, f7 = FACTORS[num[i]]
                pref2[i+1] = pref2[i] + f2
                pref3[i+1] = pref3[i] + f3
                pref5[i+1] = pref5[i] + f5
                pref7[i+1] = pref7[i] + f7
            else:
                pref2[i+1] = pref2[i]
                pref3[i+1] = pref3[i]
                pref5[i+1] = pref5[i]
                pref7[i+1] = pref7[i]

       
        if first_zero == L:
            if (pref2[L] >= c2 and pref3[L] >= c3 and 
                pref5[L] >= c5 and pref7[L] >= c7):
                return num

        
        for i in range(L - 1, -1, -1):
            if i > first_zero:
                continue
                
            rem_2 = c2 - pref2[i]
            rem_3 = c3 - pref3[i]
            rem_5 = c5 - pref5[i]
            rem_7 = c7 - pref7[i]
            
            start_digit = int(num[i]) + 1 if num[i] != '0' else 1
            
            for d in range(start_digit, 10):
                d_str = str(d)
                f2, f3, f5, f7 = FACTORS[d_str]
                
                r2, r3 = rem_2 - f2, rem_3 - f3
                r5, r7 = rem_5 - f5, rem_7 - f7
                
                rem_len = L - 1 - i
                if min_len(r2, r3, r5, r7) <= rem_len:
                    suffix = get_min_suffix(r2, r3, r5, r7)
                    pad = "1" * (rem_len - len(suffix))
                    return num[:i] + d_str + pad + suffix

      
        target_len = max(L + 1, min_len(c2, c3, c5, c7))
        suffix = get_min_suffix(c2, c3, c5, c7)
        pad = "1" * (target_len - len(suffix))
        return pad + suffix
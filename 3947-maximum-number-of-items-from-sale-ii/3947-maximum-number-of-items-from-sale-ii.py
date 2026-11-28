class Solution:
    def maximumSaleItems(self, items: list[list[int]], budget: int) -> int:
        n = len(items)
        freq = [0] * (n + 1)
        min_price = float('inf')
        
        for f, p in items:
            freq[f] += 1
            if p < min_price:
                min_price = p
                
        # Sieve to count how many items have a factor divisible by f
        mult = [0] * (n + 1)
        for f in range(1, n + 1):
            if freq[f] > 0:
                for m in range(f, n + 1, f):
                    mult[f] += freq[m]
                    
        # Collect (price, max_paired_copies) for items that can grant free copies
        paired = []
        for f, p in items:
            d = mult[f] - 1
            if d > 0:
                paired.append((p, d))
                
        paired.sort()
        
        total_items = 0
        rem = budget
        min_unbought_paired = float('inf')
        
        for p, d in paired:
            # Stop using paired copies once their effective cost (p / 2) exceeds min_price
            if p > 2 * min_price:
                min_unbought_paired = min(min_unbought_paired, p)
                break
                
            can_buy = min(d, rem // p)
            total_items += 2 * can_buy
            rem -= can_buy * p
            
            if can_buy < d:
                min_unbought_paired = min(min_unbought_paired, p)
                break
                
        # Spend remaining budget on the single cheapest item
        singles_bought = rem // min_price
        total_items += singles_bought
        rem %= min_price
        
        # Check if refunding 1 single item allows buying 1 paired copy (+2 - 1 = +1 item)
        if singles_bought > 0 and rem + min_price >= min_unbought_paired:
            total_items += 1
            
        return total_items

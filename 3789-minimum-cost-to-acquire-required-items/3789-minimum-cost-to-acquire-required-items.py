class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        # Option 1: No type 3 items
        ans = need1 * cost1 + need2 * cost2
        
        # Option 2: Cover the shared minimum requirement using type 3
        k2 = min(need1, need2)
        cost_k2 = k2 * costBoth + (need1 - k2) * cost1 + (need2 - k2) * cost2
        ans = min(ans, cost_k2)
        
        # Option 3: Cover both requirements entirely using type 3
        k3 = max(need1, need2)
        cost_k3 = k3 * costBoth
        ans = min(ans, cost_k3)
        
        return ans

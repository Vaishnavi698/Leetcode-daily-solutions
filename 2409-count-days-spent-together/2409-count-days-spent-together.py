class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        days_in_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        
        def date_to_day(date_str: str) -> int:
            month = int(date_str[:2])
            day = int(date_str[3:])
            total_days = day
            for m in range(month - 1):
                total_days += days_in_months[m]
            return total_days
            
        alice_start = date_to_day(arriveAlice)
        alice_end = date_to_day(leaveAlice)
        bob_start = date_to_day(arriveBob)
        bob_end = date_to_day(leaveBob)
        
        # Calculate overlap
        overlap_start = max(alice_start, bob_start)
        overlap_end = min(alice_end, bob_end)
        
        if overlap_start <= overlap_end:
            return overlap_end - overlap_start + 1
        return 0
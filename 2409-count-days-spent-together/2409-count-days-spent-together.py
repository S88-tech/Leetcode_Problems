from datetime import datetime, timedelta
class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        fmt = "%m-%d"
        a1 = datetime.strptime(arriveAlice, fmt)
        l1 = datetime.strptime(leaveAlice, fmt)
        a2 = datetime.strptime(arriveBob, fmt)
        l2 = datetime.strptime(leaveBob, fmt)
        
        overlap_start = max(a1, a2)
        overlap_end = min(l1, l2)
        
        if overlap_start <= overlap_end:
            return (overlap_end - overlap_start).days + 1
        return 0
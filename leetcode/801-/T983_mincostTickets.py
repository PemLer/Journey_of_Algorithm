class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        days = set(days)
        durations = [1, 7, 30]

        @lru_cache(None)
        def dp(i):
            if i > 365:
                return 0
            if i in days:
                return min(dp(i + dur) + cost for cost, dur in zip(costs, durations))
            else:
                return dp(i+1)

        return dp(1)
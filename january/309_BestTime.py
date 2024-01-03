from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cool_down, sell, hold = 0, 0, -float('inf')

        for price in prices:
            prev_cool_down, prev_sell, prev_hold = cool_down, sell, hold
            print(prev_cool_down, prev_sell, prev_hold)
            cool_down = max(prev_cool_down, prev_sell)

            sell = prev_hold + price

            hold = max(prev_hold, prev_cool_down - price)
            print("---------")
            print(prev_cool_down, prev_sell, prev_hold)
            print(cool_down, sell, hold)

        return max(sell, cool_down)
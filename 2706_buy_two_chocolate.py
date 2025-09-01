from typing import List


class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        prices.sort()

        if prices[0] + prices[1] > money:
            return money
        else:
            sum = (prices[0] + prices[1]) - money

            return sum
    

solution = Solution()
print(solution.buyChoco([3,2,3],3))
print(solution.buyChoco([1,2,2],3))
#
# @lc app=leetcode id=121 lang=python
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        if not prices:
            return 0

        # 初始化变量
        min_price = float('inf')  # 表示当前的最低买入价格
        max_profit = 0  # 表示当前的最大利润

        for price in prices:
            # 更新最低买入价格
            if price < min_price:
                min_price = price
            else:
                # 计算当前利润并更新最大利润
                max_profit = max(max_profit, price - min_price)

        return max_profit
# @lc code=end


#
# @lc app=leetcode id=2469 lang=python
#
# [2469] Convert the Temperature
#


# @lc code=start
class Solution(object):
    def convertTemperature(self, celsius):
        """
        :type celsius: float
        :rtype: List[float]
        """
        kalvin = celsius + 273.15
        fahrenheit = celsius * 1.8 + 32.00
        return [kalvin, fahrenheit]


# @lc code=end

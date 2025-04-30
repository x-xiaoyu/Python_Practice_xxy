#
# @lc app=leetcode id=1512 lang=python
#
# [1512] Number of Good Pairs
#


# @lc code=start
class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0  # 如果列表为空，返回0，注意不是 false

        count = 0
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] == nums[j]:
                    count += 1  # 计数增加1

        return count  # 返回计算的“好”数对数量


# @lc code=end

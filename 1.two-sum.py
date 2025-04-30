#
# @lc app=leetcode id=1 lang=python
#
# [1] Two Sum
#

# @lc code=start
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
            # 创建一个哈希表，用于存储数组中的数及其索引
        hashmap = {}
    
        # 遍历数组中的每个数
        for i, num in enumerate(nums):
        # 计算目标数与当前数的差值
        complement = target - num
        
        # 如果差值已经在哈希表中，说明找到了两个数
        if complement in hashmap:
            return [hashmap[complement], i]
        
        # 如果没找到，把当前数和它的索引存入哈希表
        hashmap[num] = i
        
# @lc code=end


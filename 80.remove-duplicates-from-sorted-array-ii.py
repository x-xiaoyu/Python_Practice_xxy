#
# @lc app=leetcode id=80 lang=python
#
# [80] Remove Duplicates from Sorted Array II
#

# @lc code=start
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 2:  # 如果数组长度小于等于 2，直接返回原长度
            return len(nums)
        
        # `insert_pos` 用于记录下一个可以插入的有效位置
        insert_pos = 2

        for i in range(2, len(nums)):
            # 如果当前元素和倒数第二个保留的元素不同，说明可以保留
            if nums[i] != nums[insert_pos - 2]:
                nums[insert_pos] = nums[i]  # 将当前元素插入到 `insert_pos`
                insert_pos += 1  # 移动 `insert_pos`

        return insert_pos  # 最终数组的有效长度

        
# @lc code=end


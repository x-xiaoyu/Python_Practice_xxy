#
# @lc app=leetcode id=26 lang=python
#
# [26] Remove Duplicates from Sorted Array
#

# @lc code=start
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:  # 如果数组为空，直接返回 0
            return 0

        unique_index = 0  # 指针，用于记录不重复元素的最后一个位置

        for i in range(1, len(nums)):  # 从第二个元素开始遍历
            if nums[i] != nums[unique_index]:  # 如果当前元素与上一个唯一元素不同
                unique_index += 1  # 移动指针到下一个位置
                nums[unique_index] = nums[i]  # 将当前元素放到不重复区域的下一个位置

        return unique_index + 1  # 返回不重复区域的长度

        //灵茶山艾府的答案
        k = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:  # nums[i] 不是重复项
                nums[k] = nums[i]  # 保留 nums[i]
                k += 1
        return k

        
# @lc code=end


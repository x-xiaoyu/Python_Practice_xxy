#
# @lc app=leetcode id=27 lang=python
#
# [27] Remove Element
#

# @lc code=start
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        slow = 0  # 慢指针
        for fast in range(len(nums)):  # 快指针遍历数组
            if nums[fast] != val:  # 如果当前值不是要移除的值
                nums[slow] = nums[fast]  # 将值赋给慢指针位置
                slow += 1  # 慢指针向前移动
        return slow
        # 双指针法的核心思想是用一个慢指针记录结果数组的尾部位置，另一个快指针遍历整个数组。
        # 如果快指针指向的值不是 val，就把它赋值到慢指针的位置，然后移动慢指针。
# @lc code=end


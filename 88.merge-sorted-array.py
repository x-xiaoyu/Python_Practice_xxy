#
# @lc app=leetcode id=88 lang=python
#
# [88] Merge Sorted Array
#


# @lc code=start
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        # 方法一：直接合并，然后sort 不考虑时间
        # 合并 nums2 到 nums1 的后半部分 m:意思是m是末尾，切片刀有效位置m后面
        # nums1[m:] = nums2
        # nums1.sort()

        # 第二个办法：双指针
        # 思路：
        # 使用两个指针分别指向 nums1 和 nums2 的有效部分的末尾（m-1 和 n-1）。
        # 从 nums1 的末尾（m + n - 1）开始填充较大的值。
        # 如果 nums2 有剩余，继续填充。
        # 最后，nums1 就是合并后的有序数组。
        # def merge(nums1, m, nums2, n):
        # 初始化指针
        p1 = m - 1  # nums1 有效部分的末尾
        p2 = n - 1  # nums2 的末尾
        p = m + n - 1  # nums1 的总末尾

        # 从后往前合并
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1

        # 如果 nums2 还有剩余，直接覆盖 nums1 开头
        nums1[: p2 + 1] = nums2[: p2 + 1]


# @lc code=end

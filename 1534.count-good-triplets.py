#
# @lc app=leetcode id=1534 lang=python
#
# [1534] Count Good Triplets
#


# @lc code=start
class Solution(object):
    def countGoodTriplets(self, arr, a, b, c):
        """
        :type arr: List[int]
        :type a: int
        :type b: int
        :type c: int
        :rtype: int
        """
        n = len(arr)
        count = 0
        # 使用三重循环来遍历所有可能的三元组 (i, j, k)
        for i in range(n):
            for j in range(i + 1, n):
                if abs(arr[i] - arr[j]) <= a:  # 检查第一个条件
                    for k in range(j + 1, n):
                        if (
                            abs(arr[j] - arr[k]) <= b and abs(arr[i] - arr[k]) <= c
                        ):  # 检查第二和第三个条件
                            count += 1

        return count


# @lc code=end

// Problem: 35.Search Insert Position
// Easy 1pts
// 04/11/2024
// Topics: Array, Binary Search

// Description: Given a sorted array of distinct integers and a target value,
// return the index if the target is found.
//  If not, return the index where it would be if it were inserted in order.

// Links: https://leetcode.com/problems/search-insert-position/description/

int searchInsert(int *nums, int numsSize, int target)
{
    int left = 0;
    int right = numsSize - 1;

    while (left <= right)
    {
        int mid = left + (right - left) / 2;

        if (nums[mid] == target)
        {
            return mid;
        }
        else if (nums[mid] < target)
        {
            left = mid + 1;
        }
        else
        {
            right = mid - 1;
        }
    }
    return left;
}
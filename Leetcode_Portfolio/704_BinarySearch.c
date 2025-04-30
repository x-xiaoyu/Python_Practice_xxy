// Problem: 704. Binary Search
// Easy 1pts
// 04/10/2024

// Topics: Array, Binary Search

// Description: Given an array of integers nums which is sorted in ascending order,
// and an integer target, write a function to search target in nums.
// If target exists, then return its index. Otherwise, return -1.

// Links: https://leetcode.com/problems/binary-search/description/

int search(int *nums, int numsSize, int target)
{
    int left = 0;
    int right = numsSize - 1;

    while (left <= right)
    {
        // define the mid point
        int mid = left + (right - left) / 2;

        if (nums[mid] == target)
            return mid;

        if (nums[mid] > target)
            right = mid - 1;

        else
            left = mid + 1;
    }

    return -1;
}

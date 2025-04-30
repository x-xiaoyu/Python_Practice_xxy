// Problem: 53.maximum-subarray
// Medium 2pts
// 04/24/2024
// Topics: Array, Dynamic Programming
// Description: Given an integer array nums, find the subarray with the largest sum, and return its sum.


// Links:https://leetcode.com/problems/maximum-subarray/description/

int maxSubArray(int* nums, int numsSize) {
    if (numsSize == 0) return 0; // Returns 0 if the array is empty

    int currentMax = nums[0];
    int globalMax = nums[0];

    for (int i = 1; i < numsSize; i++) {
        currentMax = (currentMax + nums[i] > nums[i]) ? currentMax + nums[i] : nums[i];
        if (currentMax > globalMax) {
            globalMax = currentMax;
        }
    }

    return globalMax;
}

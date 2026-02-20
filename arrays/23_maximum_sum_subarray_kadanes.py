"""
Problem: Maximum Subarray
Platform: LeetCode
Submission Link:
https://leetcode.com/problems/maximum-subarray/submissions/1925444029/

Submission Date: Feb 20, 2026 20:00

Submission Details:
Test Cases Passed: 210 / 210
Runtime: 40 ms (Beats 52.06%)

"""

class Solution:
    def maxSubArray(self, nums):
        curr_sum = max_sum = nums[0]
        
        for i in range(1, len(nums)):
            curr_sum = max(nums[i], curr_sum + nums[i])
            max_sum = max(max_sum, curr_sum)
        
        return max_sum
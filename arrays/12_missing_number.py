"""
Problem: Missing Number
Platform: LeetCode
Link: https://leetcode.com/problems/missing-number/submissions/1923037370/

Submission Date: Feb 18, 2026 13:44

Submission Details:
Test Cases Passed: 122 / 122
Runtime: 0 ms (Beats 100.00%)
Memory: 20.57 MB (Beats 32.52%)

"""

from ast import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        sum = 0
        for num in nums:
            sum += num
        totalSum = n * (n + 1) / 2

        return int(totalSum - sum)

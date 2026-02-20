"""
Problem: First Missing Positive
Platform: LeetCode
Link: https://leetcode.com/problems/first-missing-positive/submissions/1925065036/
Difficulty: Hard

Submission Date: Feb 20, 2026 11:29

Submission Details:
Test Cases Passed: 179 / 179
Runtime: 48 ms (Beats 57.69%)
Memory: 31.07 MB (Beats 43.27%)

"""

from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:

        # Submit kar diya hai but abhi ise acche se samjhke khud se krna hai 
        
        n = len(nums)

        for i in range(n):
            if nums[i] <= 0 or nums[i] > n:
                nums[i] = n + 1

        for num in nums:
            val = abs(num)
            if val <= n:
                nums[val - 1] = -abs(nums[val - 1])

        for i in range(n):
            if nums[i] > 0:
                return i + 1

        return n + 1
    
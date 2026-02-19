"""
Problem: Two Sum
Platform: LeetCode
Link: https://leetcode.com/problems/two-sum/submissions/1923021572/

Submission Date: Feb 18, 2026 13:23

Submission Details:
Test Cases Passed: 63 / 63
Runtime: 3 ms (Beats 52.40%)
Memory: 20.62 MB (Beats 15.43%)

"""

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(nums):
            find = target - num
            if find in seen:
                return (seen[find], i)
            seen[num] = i

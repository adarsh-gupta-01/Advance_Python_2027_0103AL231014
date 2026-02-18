"""
Problem: Move Zeroes
Platform: LeetCode
Link: https://leetcode.com/problems/move-zeroes/

Submission Date: Feb 18, 2026 10:34

Submission Details:
Test Cases Passed: 75 / 75
Runtime: 7 ms (Beats 43.01%)
Memory: 20.54 MB (Beats 47.34%)

"""

from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        num = 0
        for i in range(0, len(nums)):
            if (nums[i] != 0):
                nums[num] = nums[i]
                num += 1
        
        while (num < len(nums)):
            nums[num] = 0
            num += 1

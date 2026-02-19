"""
Problem: Move Zeroes
Platform: LeetCode
Link: https://leetcode.com/problems/move-zeroes/submissions/1922852306/

Submission Date: Feb 18, 2026 10:34

Submission Details:
Test Cases Passed: 75 / 75
Runtime: 7 ms (Beats 43.01%)
Memory: 20.54 MB (Beats 47.34%)

"""

from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        j = 0
        for i in range(0, len(nums)):
            if (nums[i] != 0):
                nums[j] = nums[i]
                j += 1
        
        while (j < len(nums)):
            nums[j] = 0
            j += 1
            
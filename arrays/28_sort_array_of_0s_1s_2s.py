"""
Problem: Sort Colors
Platform: LeetCode
Link: https://leetcode.com/problems/sort-colors/submissions/1922865418/

Submission Date: Feb 18, 2026 10:46

Submission Details:
Test Cases Passed: 89 / 89
Runtime: 0 ms (Beats 100.00%)
Memory: 19.43 MB (Beats 18.74%)

"""

from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        zero = 0
        one = 0
        two = 0
        int = 0

        for i in range(0, len(nums)):
            if (nums[i] == 0): zero += 1
            elif (nums[i] == 1): one += 1
            else: two += 1

        while (zero):
            nums[int] = 0
            zero -= 1
            int += 1

        while (one):
            nums[int] = 1
            one -= 1
            int += 1

        while (two):
            nums[int] = 2
            two -= 1
            int += 1

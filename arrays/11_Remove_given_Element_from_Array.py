"""
Problem: Remove Element
Platform: LeetCode
Submission Link:
https://leetcode.com/problems/remove-element/submissions/1925421785/

Submission Date: Feb 20, 2026

Submission Details:
Test Cases Passed: 116 / 116
Runtime: 0 ms (Beats 100.00%)

"""

from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        r = 0
        for i in range(0, len(nums)):
            if (nums[i] != val):
                nums[i], nums[r] = nums[r], nums[i]
                r += 1
        return r
"""
Problem: Rotate Array
Platform: LeetCode
Link: https://leetcode.com/problems/rotate-array/submissions/1924615481/

Submission Date: Feb 19, 2026 22:40

Submission Details:
Test Cases Passed: 40 / 40
Runtime: 3 ms (Beats 76.58%)

"""

from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        l = 0 
        k = k % len(nums)
        r = k - 1

        nums.reverse()
        
        while (l <= r):
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
        
        l = k
        r = len(nums) - 1
        while (l <= r):
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1

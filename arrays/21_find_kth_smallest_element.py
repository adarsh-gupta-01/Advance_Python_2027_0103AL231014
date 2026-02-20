
"""
Problem: Kth Smallest Element in an Array

"""

from typing import List

class Solution:
    def findKthSmallest(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums.sort()
        return nums[k - 1]

"""
Problem: Kth Largest Element in an Array
Platform: LeetCode
Submission Link:
https://leetcode.com/problems/kth-largest-element-in-an-array/submissions/1925430629/

Submission Date: Feb 20, 2026

Submission Details:
Test Cases Passed: 45 / 45
Runtime: 45 ms (Beats 91.44%)

"""

from ast import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums.sort()
        return nums[n - k]
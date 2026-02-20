"""
Problem: Find Peak Element
Platform: LeetCode
Link: https://leetcode.com/problems/find-peak-element/submissions/1919271455/

Submission Date: Feb 20, 2026 11:44

Submission Details:
Test Cases Passed: 73 / 73
Runtime: 0 ms (Beats 100.00%)
"""
from typing import List

class Solution:
    def findPeakElement(self, arr: List[int]) -> int:
        n = len(arr)
        l = 0
        r = n - 1

        while l < r:
            mid = l + (r - l) // 2

            if arr[mid] > arr[mid + 1]:
                r = mid
            else:
                l = mid + 1

        return r
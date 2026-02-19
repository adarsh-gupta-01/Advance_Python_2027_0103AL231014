"""
Problem: Merge Sorted Array
Platform: LeetCode
Link: https://leetcode.com/problems/merge-sorted-array/submissions/1924630602/

Submission Date: Feb 19, 2026 22:52

Submission Details:
Test Cases Passed: 59 / 59
Runtime: 0 ms (Beats 100.00%)

"""

from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        
        i = m - 1
        j = n - 1
        k = m + n - 1
        
        while j >= 0:
            
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            
            k -= 1
            
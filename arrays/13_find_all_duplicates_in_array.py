"""
Problem: Find All Duplicates in an Array
Platform: LeetCode
Link: https://leetcode.com/problems/find-all-duplicates-in-an-array/submissions/1924675348/

Submission Date: Feb 19, 2026 23:30

Submission Details:
Test Cases Passed: 29 / 29
Runtime: 22 ms (Beats 89.55%)

"""

from typing import List

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        
        seen = set()
        ans = []
        
        for num in nums:
            if num in seen:
                ans.append(num)
            else:
                seen.add(num)
        
        return ans

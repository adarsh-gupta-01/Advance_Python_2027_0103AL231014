"""
Problem: 2149. Rearrange Array Elements by Sign
Platform: LeetCode
Submission Link:
https://leetcode.com/problems/rearrange-array-elements-by-sign/

Submission Date: Feb 20, 2026

Submission Details:
Test Cases Passed: 133 / 133
Runtime: 43 ms (Beats 73.88%)

"""
from ast import List

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * n
        
        pos_index = 0
        neg_index = 1
        
        for num in nums:
            if num > 0:
                ans[pos_index] = num
                pos_index += 2
            else:
                ans[neg_index] = num
                neg_index += 2
        
        return ans
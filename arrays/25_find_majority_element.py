"""
Problem: Majority Element
Platform: LeetCode
Submission Link:
https://leetcode.com/problems/majority-element/submissions/1925084031/

Submission Date: Feb 20, 2026 11:48

Submission Details:
Test Cases Passed: 53 / 53
Runtime: 4 ms (Beats 71.11%)
Memory: 21.21 MB (Beats 37.77%)

"""

class Solution:
    def majorityElement(self, nums):
        cd = 0
        count = 0
        
        for num in nums:
            if count == 0:
                cd = num
            
            if num == cd:
                count += 1
            else:
                count -= 1
        
        return cd
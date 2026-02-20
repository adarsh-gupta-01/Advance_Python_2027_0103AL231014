"""
Problem: Find the Middle Index in Array
Platform: LeetCode
Link: https://leetcode.com/problems/find-the-middle-index-in-array/

Time Complexity: O(n)
Space Complexity: O(1)

"""

from typing import List

class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        total_sum = sum(nums)
        left_sum = 0
        
        for i in range(len(nums)):
            right_sum = total_sum - left_sum - nums[i]
            
            if left_sum == right_sum:
                return i
            
            left_sum += nums[i]
        
        return -1

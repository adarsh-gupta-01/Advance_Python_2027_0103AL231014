"""
Problem: Maximum Difference Between Larger and Smaller Value
Platform: GeeksforGeeks
Link: https://www.geeksforgeeks.org/maximum-difference-between-any-two-elements/

"""

from typing import List

class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return -1
        
        min_so_far = nums[0]
        max_diff = -1
        
        for i in range(1, len(nums)):
            diff = nums[i] - min_so_far
            
            if diff > max_diff:
                max_diff = diff
            
            if nums[i] < min_so_far:
                min_so_far = nums[i]
        
        return max_diff

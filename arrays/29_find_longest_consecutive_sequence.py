"""
Problem: Longest Consecutive Elements
Platform: LeetCode
Link: https://leetcode.com/problems/longest-consecutive/

Time Complexity: O(n)
Space Complexity: O(n)

"""

from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if not nums:
            return 0
        
        num_set = set(nums)
        max_length = 0
        
        for num in num_set:
            if num - 1 not in num_set:
                current_num = num
                current_length = 1
                
                while current_num + 1 in num_set:
                    current_num += 1
                    current_length += 1
                
                max_length = max(max_length, current_length)
        
        return max_length

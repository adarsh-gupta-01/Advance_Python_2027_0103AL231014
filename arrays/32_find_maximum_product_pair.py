"""
Problem: Maximum Product of Two Elements in Array
Platform: LeetCode
Link: https://leetcode.com/problems/maximum-product-of-word-lengths/

"""

from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        
        max1 = max2 = float('-inf')
        min1 = min2 = float('inf')
        
        for num in nums:
            if num > max1:
                max2 = max1
                max1 = num
            elif num > max2:
                max2 = num
            
            if num < min1:
                min2 = min1
                min1 = num
            elif num < min2:
                min2 = num
        
        # Maximum product: either two largest positives or two smallest negatives
        
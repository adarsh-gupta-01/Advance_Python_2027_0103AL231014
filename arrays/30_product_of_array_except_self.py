"""
Problem: Product of Array Except Self
Platform: LeetCode
Link: https://leetcode.com/problems/product-of-array-except-self/

Time Complexity: O(n)
Space Complexity: O(n) for output array

"""

from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [1] * n

        for i in range(1, n):
            result[i] = result[i - 1] * nums[i - 1]
        
        right_product = 1
        for i in range(n - 1, -1, -1):
            result[i] *= right_product
            right_product *= nums[i]
        
        return result

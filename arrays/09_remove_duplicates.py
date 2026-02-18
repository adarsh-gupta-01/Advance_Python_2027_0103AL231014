"""
Problem: Remove Duplicates from Sorted Array
Platform: LeetCode 
Link: https://leetcode.com/problems/remove-duplicates-from-sorted-array/submissions/1922484446/
Submission Date: Feb 17, 2026 23:42

Submission Details:
Test Cases Passed: 362 / 362
Runtime: 0 ms (Beats 100.00%)
Memory: 20.54 MB (Beats 52.98%)

Learning:
1. Understood the Two-Pointer Technique.
2. Learned how to modify array in-place.
3. Used one pointer (i) to track unique elements.
4. Used second pointer (j) to scan the array.
5. Learned that function returns length of unique elements (i + 1).
6. Practiced handling edge case: empty array.
7. Strengthened understanding of sorted array property.
"""

from ast import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        i = 0
        
        for j in range(1, len(nums)):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]
        
        return i + 1

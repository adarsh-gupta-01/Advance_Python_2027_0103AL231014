"""
Problem: Two Sum
Platform: LeetCode
Link: https://leetcode.com/problems/two-sum/

Submission Date: Feb 18, 2026 13:23

Submission Details:
Test Cases Passed: 63 / 63
Runtime: 3 ms (Beats 52.40%)
Memory: 20.62 MB (Beats 15.43%)

Learning:
1. Learned HashMap (dictionary) based approach.
2. Understood complement technique:
       find = target - num
3. Learned how to check existence in O(1) using dictionary.
4. Practiced using enumerate() for index + value together.
5. Improved thinking from brute-force O(n²) to optimized O(n).
6. Strengthened understanding of time-space tradeoff.

Concept:
- Store previously seen numbers in dictionary.
- For each element, check if its complement already exists.
- If yes → return indices immediately.
"""

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(nums):
            find = target - num
            if find in seen:
                return (seen[find], i)
            seen[num] = i

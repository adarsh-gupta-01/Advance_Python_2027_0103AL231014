"""
Problem: Subarray Sum Equals K
Platform: LeetCode
Link: https://leetcode.com/problems/subarray-sum-equals-k/

Submission Date: Feb 20, 2026 11:05

Submission Details:
Test Cases Passed: 93 / 93
Runtime: 31 ms (Beats 72.84%)
Memory: 21.86 MB (Beats 67.85%)

"""

from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        curr_sum = 0
        prefix = {0: 1}

        for num in nums:
            curr_sum += num

            if curr_sum - k in prefix:
                count += prefix[curr_sum - k]

            prefix[curr_sum] = prefix.get(curr_sum, 0) + 1

        return count
"""
Problem: Sum of Array
Platform: GeeksforGeeks
Link: https://www.geeksforgeeks.org/problems/sum-of-array2326/1

Submission Details:
Test Cases Passed: 1115 / 1115
Attempts: 2 / 2
Accuracy: 100%
Time Taken: 0.17 seconds

Learning:
1. Python is indentation-sensitive.
2. The 'return' statement must be properly aligned inside the function.
3. Misaligned indentation causes runtime or syntax errors.
"""

# User function Template for python3
class Solution:
    def arraySum(self, arr):
        total = 0
        
        for num in arr:
            total += num
        
        return total

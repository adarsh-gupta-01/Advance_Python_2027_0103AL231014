"""
Problem: Reverse an Array
Platform: GeeksforGeeks
Link: https://www.geeksforgeeks.org/problems/reverse-an-array/1

Submission Details:
Date: 2026-02-17 22:32:10
Status: Correct
Language: Python 3
Test Cases Passed: 1115 / 1115

"""

class Solution:
    def reverseArray(self, arr):
        l = 0
        r = len(arr) - 1 
        
        while l < r:
            arr[l], arr[r] = arr[r], arr[l]
            l += 1 
            r -= 1 
            
        return arr
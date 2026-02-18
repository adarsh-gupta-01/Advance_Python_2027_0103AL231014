"""
Problem: Find Minimum and Maximum Element in an Array
Platform: GeeksforGeeks
Link: https://www.geeksforgeeks.org/problems/find-minimum-and-maximum-element-in-an-array4428/1

Submission Details:
Test Cases Passed: 1111 / 1111
Points Scored: 1 / 1
Total Score: 140
Time Taken: 0.06 seconds

Learning:
1. Python does not use 'else if' like other languages.
2. Python uses 'elif' for else-if conditions.

"""

class Solution:
    def getMinMax(self, arr):
        
        max = arr[0]
        min = arr[0]

        for i in range(1, len(arr)):
            
            if arr[i] > max:
                max = arr[i]
            
            if arr[i] < min:
                min = arr[i]

        return min, max

"""
Problem: Second Largest Element in an Array
Platform: GeeksforGeeks
Link: https://www.geeksforgeeks.org/problems/second-largest3735/1

Submission Details:
Test Cases Passed: 1120 / 1120
Time Taken: 0.24 seconds


"""

class Solution:
    def getSecondLargest(self, arr):
        l = -1
        sl = -1
        
        for i in range(0, len(arr)):
        
            if (arr[i] > l):
                sl = l
                l = arr[i]
                
            elif (arr[i] < l and arr[i] > sl):
                sl = arr[i]
        
        return sl

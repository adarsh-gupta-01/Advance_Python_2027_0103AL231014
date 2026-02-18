"""
Problem: Frequency of Array Elements
Platform: GeeksforGeeks
Link: https://www.geeksforgeeks.org/problems/frequency-of-array-elements-1587115620/1

Submission Details:
Test Cases Passed: 1111 / 1111
Attempts: 1 / 1
Accuracy: 100%
Points Scored: 2 / 2
Total Score: 144
Time Taken: 1.81 seconds

"""

class Solution:
    def frequencyCount(self, arr):
        
        ans = [0] * len(arr)
        
        for i in range(0, len(arr)):
            n = arr[i]
            ans[n-1] += 1
            
        return ans

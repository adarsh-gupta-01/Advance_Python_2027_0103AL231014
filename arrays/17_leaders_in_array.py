"""
Problem: Leaders in an Array
Platform: GeeksforGeeks
Link: https://www.geeksforgeeks.org/problems/leaders-in-an-array-1587115620/1

Submission Details:
Test Cases Passed: 1111 / 1111
Attempts: 1 / 1
Accuracy: 100%
Points Scored: 2 / 2
Total Score: 152
Time Taken: 0.07 seconds

"""

class Solution:
    def leaders(self, arr):
        
        n = len(arr)
        mx = arr[n-1]
        ans = []
        
        for i in range(n-1, -1, -1):
            
            if arr[i] >= mx:
                ans.append(arr[i])
                mx = arr[i]
        
        ans.reverse()
        return ans

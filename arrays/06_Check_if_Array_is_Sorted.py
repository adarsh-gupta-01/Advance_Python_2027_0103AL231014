"""
Problem: Check if an Array is Sorted
Platform: GeeksforGeeks
Link: https://www.geeksforgeeks.org/problems/check-if-an-array-is-sorted0701/1

Submission Details:
Test Cases Passed: 1112 / 1112
Attempts: 1 / 1
Accuracy: 100%
Points Scored: 2 / 2
Total Score: 142
Time Taken: 0.46 seconds

Mistakes Identified & Corrected:
1. Python uses capitalized boolean values:
       False and True
   (not false or true)

2. This condition was unnecessary:
       if (arr[len(arr)-1] < arr[0]):
   Because checking adjacent elements already ensures
   whether the array is sorted.

"""

class Solution:
    def isSorted(self, arr) -> bool:
        for i in range(0, len(arr)-1):
            if (arr[i] > arr[i+1]):
                return False
                
        return True

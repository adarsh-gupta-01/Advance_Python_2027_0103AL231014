"""
Problem: Check if Two Arrays are Equal or Not
Platform: GeeksforGeeks
Link: https://www.geeksforgeeks.org/problems/check-if-two-arrays-are-equal-or-not3847/1

Submission Details:
Test Cases Passed: 1112 / 1112
Attempts: 1 / 1
Accuracy: 100%
Points Scored: 2 / 2
Total Score: 146
Time Taken: 0.94 seconds

"""

class Solution:
    def checkEqual(self, a, b) -> bool:
        
        if len(a) != len(b):
            return False
        
        count = {}
        
        for num in a:
            count[num] = count.get(num, 0) + 1
        
        for num in b:
            if num not in count:
                return False
            count[num] -= 1
            if count[num] < 0:
                return False
        
        return True

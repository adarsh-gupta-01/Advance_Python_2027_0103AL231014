"""
Problem: Union of Two Sorted Arrays
Platform: GeeksforGeeks
Link: https://www.geeksforgeeks.org/problems/union-of-two-sorted-arrays-1587115621/1

Submission Details:
Test Cases Passed: 1115 / 1115
Attempts: 1 / 3
Accuracy: 33%
Points Scored: 4 / 4
Total Score: 150
Time Taken: 0.92 seconds


Important Mistake Learned:

❌ ans = list(set1 or set2)

In Python:
    set1 or set2

Means:
    - If set1 is non-empty → return set1
    - Otherwise → return set2

It does NOT combine both sets.

✅ Correct union operation:
    set1 | set2
"""

class Solution:
    def findUnion(self, a, b):
        
        set1 = set(a)
        set2 = set(b)
        
        ans = list(set1 | set2)
        
        ans.sort()
        
        return ans

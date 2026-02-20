class Solution:
    def rotateLeft(self, arr, d):
        n = len(arr)
        
        if n == 0:
            return arr
        
        d = d % n 
        
        def reverse(l, r):
            while l < r:
                arr[l], arr[r] = arr[r], arr[l]
                l += 1
                r -= 1

        reverse(0, d - 1)
        reverse(d, n - 1)
        reverse(0, n - 1)
        
        return arr


def main():
    arr = list(map(int, input("Enter array elements separated by space: ").split()))
    d = int(input("Enter number of rotations: "))
    
    sol = Solution()
    result = sol.rotateLeft(arr, d)
    
    print("Array after left rotation:", result)


if __name__ == "__main__":
    main()
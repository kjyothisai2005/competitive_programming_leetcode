class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(arr)
        
        # Step 1: Find Previous Less Element (PLE)
        ple = [-1] * n
        stack = []
        for i in range(n):
            while stack and arr[stack[-1]] > arr[i]:
                stack.pop()
            ple[i] = stack[-1] if stack else -1
            stack.append(i)
        
        # Step 2: Find Next Less Element (NLE)
        nle = [n] * n
        stack = []
        for i in range(n-1, -1, -1):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            nle[i] = stack[-1] if stack else n
            stack.append(i)
        
        # Step 3: Calculate contribution
        res = 0
        for i in range(n):
            left = i - ple[i]
            right = nle[i] - i
            res = (res + arr[i] * left * right) % MOD
        
        return res

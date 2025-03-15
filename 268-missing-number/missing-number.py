class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        k=0
        for i in range(n+1):
            if i not in nums:
                k=i
        return k
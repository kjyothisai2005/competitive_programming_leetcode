class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        n=len(nums)
        min_pos=-1
        max_pos=-1
        temp=-1
        fixed_bound=0
        for st in range(n):
            if(nums[st]<minK or nums[st]>maxK):
                temp=st
            if(nums[st]==minK):
                min_pos=st
            if(nums[st]==maxK):
                max_pos=st
            fixed_bound+=max(0,min(min_pos,max_pos)-temp)
        return fixed_bound 
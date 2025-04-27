class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        l=[]
        cnt=0
        for i in range(len(nums)-2):
            l=nums[i:i+3]
            if((l[0]+l[2])==(l[1]/2)):
                cnt+=1
        return cnt
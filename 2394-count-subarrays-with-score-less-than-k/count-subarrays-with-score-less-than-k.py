class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        lsum=0
        subarrays=0
        cnt=0
        for i in range(len(nums)):
            cnt+=nums[i]
            while(i-lsum+1)*cnt>=k:
                cnt-=nums[lsum]
                lsum+=1
            subarrays+=(i-lsum+1)
        return subarrays
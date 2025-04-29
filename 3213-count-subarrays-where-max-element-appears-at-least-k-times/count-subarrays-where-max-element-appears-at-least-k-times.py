class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        cnt=0
        l=0
        mx_ele=max(nums)
        cnt_max=0
        for i in range(len(nums)):
            if nums[i]==mx_ele:
                cnt_max+=1
            while(cnt_max>=k):
                cnt+=(len(nums)-i)
                if nums[l]==mx_ele:
                    cnt_max-=1
                l+=1
        return cnt
class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        cnt=0
        for i in nums:
            st=str(i)
            if(len(st)%2==0):
                cnt+=1
        return cnt
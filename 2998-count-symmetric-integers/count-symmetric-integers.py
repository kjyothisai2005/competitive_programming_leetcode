class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        cnt=0
        for i in range(low,high+1):
            if len(str(i)) %2== 0:
                s=str(i)
                st1,st2=s[:len(s)//2],s[len(s)//2:]
                sum1=sum(int(x) for x in st1)
                sum2=sum(int(x) for x in st2)
                if sum1==sum2 :
                    cnt+=1
        return cnt
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        l=[]
        for i in s.split():
            l.append(i)
        return len(l[len(l)-1])
class Solution:
    def clearDigits(self, s: str) -> str:
        s=list(s)
        d=0
        for i in range(len(s)):
            if s[i].isalpha():
                s[d]=s[i]
                d+=1
            if s[i].isdigit():
                d-=1
        s=s[:d]
        return "".join(s)
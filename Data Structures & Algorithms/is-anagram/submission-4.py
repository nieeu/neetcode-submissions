class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        countS, countT = {}, {}
        for i in range(len(s)):
            countS[s[i]] = 1+ countS.get(s[i],0) # return 0 if s[i] 
                                                    # not in string
            countT[t[i]] = 1+ countT.get(t[i],0)

        return countS == countT
class Solution:
    # from collections import defaultdict
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) # if key not exist, create the 
                            # key and assign it an empty list [].
        for s in strs:
            ls = [0]*26
            for c in s:
                ls[ord(c)-ord("a")] +=1
            res[tuple(ls)].append(s)
        return list(res.values())
    

        
            
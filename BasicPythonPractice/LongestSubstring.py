#Given a string, find the length of the longest substring without repeating characters
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=[]
        nl=[]
        num=[]

        if len(s)==0:
            res = 0
        for a in range(0,len(s)):
            num.append(a)
        
        for j in num:
            for i in range(j,len(s)):
                if s[i] not in l:
                    l.append(s[i])
                else:
                    #num.append(i)
                    break
            nl.append(len(''.join(l)))
            l.clear()
            res=max(nl)
        return(res)
        
    
Solution().lenOfLongestSubstring('abrkaabcdefghijjxxx') 

#TestCase1: abrkaabcdefghijjxxx: 10
#TestCase2: dvdf: 3
#TestCase3: '': 0

#Given a string, find the length of the longest substring without repeating characters
class Solution:
    def lenOfLongestSubstring(self,s):
        str = ''
        for i in range(0,len(s)-1):
            if s[i] != s[i-1]:
                str = str + s[i]
            else:
                break
        return(len(str))
    
Solution().lenOfLongestSubstring('abrkaabcdefghijjxxx')

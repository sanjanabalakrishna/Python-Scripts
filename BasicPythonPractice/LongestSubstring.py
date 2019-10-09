#Given a string, find the length of the longest substring without repeating characters
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substring = ''
        di = {}
        
        if len(s) < 2:
            return(len(s))
        for char in s:
            if char not in substring:
                substring += char
            else:
                di[substring] = len(substring)
                substring = substring[substring.index(char)+1:]
                substring += char
        di[substring] = len(substring)
        return(max(di.values()))
        
    
Solution().lenOfLongestSubstring('abrkaabcdefghijjxxx') 

#TestCase1: abrkaabcdefghijjxxx: 10
#TestCase2: dvdf: 3
#TestCase3: '': 0

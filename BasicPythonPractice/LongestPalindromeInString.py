#Given a string s, find the longest palindromic substring in s
class Solution:
    def longestPalindrome(self, s: str) -> str:
        sub = ''
        longestsub=''

        if len(s) < 2:
            return(s)
        else:
            for i in range(len(s)):
                for j in range(len(s),i,-1):
                    sub = s[i:j]
                    if sub == sub[::-1] and len(sub) > len(longestsub):
                        longestsub=sub
        return(longestsub)

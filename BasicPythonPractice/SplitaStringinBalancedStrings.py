#Balanced strings are those who have equal quantity of 'L' and 'R' characters.
#Given a balanced string s split it in the maximum amount of balanced strings
#Return the maximum amount of splitted balanced strings.

class Solution:
    def balancedStringSplit(self, s):
        dups = s
        sub = ''
        lst = []
        maxi = 0
        
        while maxi < len(s)-1:
            for i in range(len(s)):
                if len(dups)!=0 and (sub == '' or (len(sub.replace('R','')))!= (len(sub.replace('L','')))):
                    sub = sub + dups[i]
                    if sub==s:
                        maxi=len(s)
                        lst.append(sub)
                        break    
                else:
                    lst.append(sub)
                    dups = dups[i:]
                    sub = ''
                    if len(dups)!=0:
                        maxi=i
                    else:
                        maxi=len(s)
                    break        
        
        return(len(lst))
s= 'RLRRLLRLRL'          
Solution().balancedStringSplit(s) 

'''TestCases: 
1.
Input: s = "RLRRLLRLRL"
Output: 4
Explanation: s can be split into "RL", "RRLL", "RL", "RL", each substring contains same number of 'L' and 'R'.
        
2.
Input: s = "RLLLLRRRLR"
Output: 3
Explanation: s can be split into "RL", "LLLRRR", "LR", each substring contains same number of 'L' and 'R'.

3.
Input: s = "LLLLRRRR"
Explanation: s can be split into "LLLLRRRR".
Output: 1
'''
            

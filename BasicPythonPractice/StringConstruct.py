#Given an arbitrary ransom note string and another string containing letters from all the magazines, 
#Write a function that will return true if the ransom note can be constructed from the magazines ; otherwise, it will return false.
#Each letter in the magazine string can only be used once in your ransom note.
#Note: You may assume that both strings contain only lowercase letters.
#canConstruct("a", "b") -> false
#canConstruct("aa", "ab") -> false
#canConstruct("aa", "aab") -> true

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        d1={}
        for i in ransomNote:
            d1[i]=d1.get(i,0)+1
        for k,v in d1.items():
            if magazine.count(k)>=v:
                continue
            else:
                return(False)
                break  
        return(True)
        
        
#Old Solution:
#class Solution:
#    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
#        d1={}
#        d2={}
#        l=[]
#        for i in ransomNote:
#            d1[i]=d1.get(i,0)+1
#        for j in magazine:
#            d2[j]=d2.get(j,0)+1
#        for k,v in d1.items():
#            if k in d2.keys() and d1[k]<=d2[k]:
#                continue
#            else:
#                l.append(v)
#        return(len(l)==0)

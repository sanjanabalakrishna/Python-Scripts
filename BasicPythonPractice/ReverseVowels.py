#Write a function that takes a string as input and reverse only the vowels of a string.
class Solution:
    def reverseVowels(self, s: str) -> str:
        lst=[]
        l = list(s)
        for i in range(len(l)):
            if l[i] in ['a','e','i','o','u','A','E','I','O','U']:
                lst.append(i)
        while len(lst)!=0:
            mi,ma=min(lst),max(lst)
            l[mi],l[ma]=l[ma],l[mi]
            if mi!=ma:
                lst.pop(lst.index(mi))
                lst.pop(lst.index(ma))
            else:
                lst.pop(lst.index(ma))
        s1=''.join(l)
        return(s1)

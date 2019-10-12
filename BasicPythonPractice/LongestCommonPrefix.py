class Solution:
    def longestCommonPrefix(self, strs):
        #If input list is empty, return ''
        if len(strs) == 0:
            return ""
        #If input list has only one word, return the word
        elif len(strs) == 1:
            return(strs[0])
        else:     
            #Take the smallest word in the list to compare against the list 
            prefix = min(strs, key = len)
            #Remove that word from list for fewer iterations
            strs.pop(strs.index(prefix))
        
            for i in range(len(strs)):
                #As long as there is no word starting with the prefix
                while ((strs[i].find(prefix))!=0) :
                    #Remove last letter from prefix
                    prefix = prefix[:-1]
                    if prefix == '':
                        return prefix
            return prefix

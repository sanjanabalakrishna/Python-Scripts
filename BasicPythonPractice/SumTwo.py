#Given an array of integers, return indices of the two numbers such that they add up to a specific target.
#You may assume that each input would have exactly one solution, and you may not use the same element twice.

class Solution:
    def SumTwo(self, nums, target):
        di = {n:i for i,n in enumerate(nums)} #Create a dictionary with number and its index
        for i,j in enumerate(nums):
            x = target - j                    #Subtract number from target and check if that number is in the dictionary
            if x in di:
                return(i,di[x])
nums = [0,7,11,2]
target = 9
Solution().SumTwo(nums, target)

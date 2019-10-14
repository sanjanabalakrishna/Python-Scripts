#Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
#An input string is valid if:
#Open brackets must be closed by the same type of brackets.
#Open brackets must be closed in the correct order.

class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)< 1:
            return True
        elif ((len(s))%2) != 0:
            return False
        else:
            di = {'(':')','[':']','{':'}'}
            lst = []
            for i in s:
                if i in di:
                    lst.append(i)
                else:
                    if lst and i == di[lst.pop()]:
                        continue
                    else:
                        return(False)
        return(len(lst) == 0)

newlist = []

def flatten(lst):
    for item in lst:
        if isinstance(item,list)==True:
            flatten(item)
        else:
            newlist.append(item)
 
l = [1,2,[3,4],5,[6,7,[8,'a']]]

flatten(l)
print(newlist)

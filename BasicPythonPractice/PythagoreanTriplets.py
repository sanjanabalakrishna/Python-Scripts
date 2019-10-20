#
l = [3,6,12,5,13]
lp=[]
trip=[]
target=0
for i in l:
    lp.append(i**2)
for j in range(len(lp)):
    #print('Target:',lp[j])
    target=lp[j]
    for n in lp:
        #print('target-n',target,n,target-n)
        x = target - n
        if x in lp and  x not in trip:
            trip.append((x,n,target))
    
trip

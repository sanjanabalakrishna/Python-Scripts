inp = open(input('Enter a filename:'))
lst = []
di = {}
for line in inp:
    words = line.strip().split()
    if len(words)==0 or words[0]!='From':
        continue
    for num in words:
        if ':' in num:
            hour = num.split(':')
            lst.append(hour[0])
for i in lst:
    di[i] = di.get(i,0) + 1

tuplist = sorted([(k,v) for k,v in di.items()])

for x,y in tuplist:
    print(x,y)

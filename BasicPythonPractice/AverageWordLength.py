inp = open(input('Enter a file:'))
lst = []
sum = 0

#Create a list of the unique words in the file
for line in inp:
    words = line.strip().split()
    for word in words:
        if word not in lst:
        	lst.append(word)
            
#Count number of words            
Cnt = len(lst)

#Add the lengths of each word
for wrd in lst:
    sum += len(wrd)
    
print('Average word length in the file is:',round(sum/Cnt))

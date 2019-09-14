inp = open(input('Enter a file:'))
n = input('How many commonly used words would you like to check?:')
lst = []
di = {}

#Create a list of the words in the file
for line in inp:
    words = line.strip().split()
    for word in words:
        lst.append(word)

#Count occurance of each word
for wrd in lst:
    di[wrd] = di.get(wrd,0) + 1

#Sort the dictionary is descending order of value
tuplist = sorted([(v,k) for k,v in di.items()], reverse = True)

#Slice the inout number of words
mostused = tuplist[0:n]

#Print the words
print(n,'most commonly used words are:')
for i,j in mostused:
    print(j)

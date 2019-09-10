#Function to always return number less than equal to 25
def AlphabetKey(x):
    if x > 25:
        while x > 25:
            y = x - 25
            x = y
        return(y)
    else:
        return(x)


alphabet = 'abcdefghijklmnopqrstuvwxyz'
spcl = ['+','=','-','_','`','~',',','.','?','/','>','<',':',':','"','!','@',' ','#','$','%','^','&','*','(',')','1','2','3','4','5','6','7','8','9','0']
a = []
ind = []
EncIndex = list()
inp = input('Enter a secret message:').lower()
try:
    UserKey = int(input('Enter a key:'))
    Key = AlphabetKey(UserKey)
    
    #Create two lists for the letter and the index
    for i,j in enumerate(alphabet):
        a.append(j)
        ind.append(i)
    
    #Create a dictionary out of the two lists
    di = dict(zip(a,ind))
    
    for z in inp:
        if not z in spcl: 
            newind= di[z]+Key 
            if newind < 25: #If user entered a number > 25, call function
                print(''.join([key for key,value in di.items() if value == newind]), end = '') #This is to get key using value from dictionary
            else:
                newind = AlphabetKey(newind)
                print(''.join([key for key,value in di.items() if value == newind]), end = '') #End = '' prints without /n or space
        else:
            print(z, end = '')
except:
    print('Enter a valid key')

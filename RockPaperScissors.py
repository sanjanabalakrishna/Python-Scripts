import random as r

#Take player and computer input
def play():
    player = input('Enter Rock/Paper/Scissors:').upper()
    asgn = {1: 'ROCK', 2: 'PAPER', 3: 'SCISSORS'}
    cpu = asgn[r.randint(1,3)]
    return(cpu,player)

#Compute which combination wins
def compare(cpu,player):
    result = {('ROCK','PAPER') : True,
              ('ROCK','SCISSORS') : False,
              ('PAPER', 'SCISSORS') : True,
              ('PAPER', 'ROCK') : False,
              ('SCISSORS', 'ROCK') : True,
              ('SCISSORS', 'PAPER') : False}
    return result[cpu,player]

inp = input('Do you want to play rock paper scissors? Y/N:').capitalize()
while True:
    if inp != 'N' and inp != 'Y':
        print('Error! Enter Y or N')
        break
    if inp == 'N':
        print('Game Over')
        break
    else:
        c,p=play()
        if p not in ['ROCK','PAPER','SCISSORS']:
            print('Error! Enter a valid input. Choose from: Rock/Paper/Scissors')
        if c==p:
            print('Draw!')
            break
        else:
            print('Computer played:',c, 'and you played:',p)
            if compare(c,p) == True:
                print('You won')
                break
            else:
                print('You lost')
                break

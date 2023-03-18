import random
a=int(input('Enter 1 for stone\nEnter 2 for paper\nEnter 3 for scissor\n'))
if a==1:

    print('you chose stone')
elif a==2:
    print('you chose paper')
elif a==3:
    print('you chose scissor')
c=('scissor','paper','stone')
b=random.choice(c)
print('your opponent chose',b)
if a==b:
    print('draw')
elif a==1:
    if b=='paper':
        print('you  win')
    elif b=='scissor':
        print('you win')
elif a==2:
    if b=='stone':
        print('you lose')
    elif b=='scissor':
        print('you lose')
elif a==3:
    if b=='stone':
        print('you lose')
    elif b=='paper':
        print('you win')

    

        

    

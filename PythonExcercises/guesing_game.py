####Importy
from random import randint
###PROGRAM
print('Guesing game')
print("Tap number from 1 to 9 exit to quit")

a=0
i=0
AI_chose = randint(1,9)
while(a != AI_chose):
    i=i+1
    a=input('Your chose is:')
    if a == 'exit':
        exit()
    a=int(a)
    if a==AI_chose:
        print('You guesed')
        print('you needed tryes')
        print(i)
        input('Tap exit to quit or anything to play again')
        a = 0
        i=0
        AI_chose = randint(1, 9)
    elif a<AI_chose:
        print('Too low')
    elif a>AI_chose:
        print("Too high")



import random
a='1234567890123456789012345678901234567890'
AI_chose=''.join(random.sample(a,4))
print('welcome to cows and bulls game')
print(AI_chose)
b=[0,1,2,3]

bulls=0
cows=0
us_chose=input('podaj 4 cyfrową liczbę')
for i in b:
    for j in b:
        if i==j:
            if AI_chose[i]==us_chose[j]:
                bulls+=1
        else:
            if AI_chose[i]==us_chose[j]:
                cows+=1
print(AI_chose)
print(us_chose)
print(cows)
print(bulls)

#AAABBBCCCAAABBB
#3A3B3C3A3B
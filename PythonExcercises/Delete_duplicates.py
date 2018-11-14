def de_duv1(x):
    y=[]
    for i in x:
        if i not in y:
            y.append(i)
    return y

def de_duv2(x):
    return(set(x))

a = [1,2,3,4,3,2,1]
print(de_duv1(a))
print(de_duv2(a))
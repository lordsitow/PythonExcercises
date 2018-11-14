def fibonaci(n):
    if n==1:
        num=1
    elif n==2:
        num=1
    else:
        num=fibonaci(n-1)+fibonaci(n-2)
    return num
print(fibonaci(int(input('Z jakiej liczby chcesz policzyć fibo?'))))
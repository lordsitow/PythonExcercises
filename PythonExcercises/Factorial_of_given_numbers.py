def factorial(i):
    if i == 0:
        return 1
    elif i == 1:
        return 1
    elif i < 0:
        print("nie ma silnie z liczby ujemnej")

    return i * factorial(i - 1)

print(factorial(5))
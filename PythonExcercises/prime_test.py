def is_prime(number):
    '''Returns True for prime numbers, False otherwise'''
    #Edge Cases
    if number == 1:
        prime = False
    elif number == 2:
        prime = True
    #All other primes
    else:
        prime = True
        for check_number in range(2, int((number / 2)+1)):
            if number % check_number == 0:
                prime = False
                break
    return prime


a = is_prime(int(input('podaj liczbe')))
if a == 1:
    print('jest pierwsza')
else:
    print('nie jest pierwsza')
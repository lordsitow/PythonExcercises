import random

def gen_pass(level,passlen):
    symbols="qwertyuiopasdfghjkl"
    if level=="weak":
        return ''.join(random.sample(symbols, passlen))
    if level=='medium':
        symbols='qwertyuip1234567890'
        return ''.join(random.sample(symbols, passlen))
    if level == 'hard':
        symbols='QWERTYUIOqwertyuiop1234567890'
        return ''.join(random.sample(symbols, passlen))
    if level == 'very hard':
        symbols = 'QWERTYUYIqwertyuiop1234567890!@#$%^&*()'
        return ''.join(random.sample(symbols, passlen))


print(gen_pass(input('level of pass'),int(input('pass length'))))
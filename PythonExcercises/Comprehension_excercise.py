import random

a = random.sample(range(10), 7)
b = random.sample(range(10), 6)

new_list = [i for i in a if i in b]

print(new_list)
import random

x = random.random()
print(x)

import random
x = random.randrange(1111,9999)
print(x)


import random
x = random.randint(1111,9999)
print(x)

import random
list1 = ('fath','fathima','paathu')
x = random.choice(list1)
print(x)

import random
list1 = ['fath','fathima','paathu', 'nasrin','ke']
x = random.shuffle(list1)
print(list1)

import random
list1 = ['fath','fathima','paathu', 'nasrin','ke']
x = random.sample(list1,2)
print(x)

import random
list1 = ['fath','fathima','paathu', 'nasrin','ke']
x = random.sample(list1,3)
print(x)


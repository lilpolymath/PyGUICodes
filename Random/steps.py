'''
from random import randint

steps = 7
one_count = 0
two_count = 0
ongoing = steps
reached = False

while reached == False:
    goto = randint(1,2)
    if goto == 1:
        one_count += 1
    if goto == 2:
        two_count += 1
    ongoing = ongoing - goto
    if ongoing == 0:
        reached = True

print('Reached Using', one_count, 'ones and',two_count, ' twos')
'''


def F(n):
    if n <= 1:
        return n
    return F(n-1) + F(n-2)

def countWays(s):
    return F(s + 1)

s = 4
while s < 8:
    print("Number of ways for ", s)
    print(countWays(s))
    s += 1

'''
while s < 8:
    print("Number of ways for ", s)
    print(countWays(s))
    s += 1
'''

'''
greetings = ['Hello', 'Guys']

for x in greetings:
    print(x)
'''

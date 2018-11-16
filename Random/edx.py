x = int(input('Number to square: '))
ans = 0
itersleft = x
while (itersleft != 0):
    ans = ans + x
    itersleft -= 1

print( str(x ) + '*' + str(x) + '=' + str(ans))

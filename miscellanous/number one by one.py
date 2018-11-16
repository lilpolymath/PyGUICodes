num = int(input('The number: '))
def prin(num):
    if num < 10:
        print(num)
    else:
        prin(num//10)
        print(num%10)

prin(num)

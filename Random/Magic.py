def MagicSquare(n):
    Square = [[0 for x in range(n)] for y in range(n)]
    i = int(n/2)
    j = int(n - 1)
    num = 1
    while num <= (n*n):
        if i == -1 and j == n:
            j = n - 2
            i = 0
        else:
            if j == n:
                j = 0
            if i < 0:
                i = n - i
        if Square[i][j]:
            j = j - 2
            i = i + 1
            continue
        else:
            Square[i][j] = num
            num += 1
        j = j + 1
        i = i - 1
        print("Magic Square for n = ", n)
        print("Sum of each row or column = ", (n**3 + n)/2)
        for i in range(0,n):
            for j in range(0, n):
                print("%2d" %(Square[i][j]))
            print()

MagicSquare(3)
array = [1,2,3,4,5,6,7,8,9]
find = int(input("Number to search: "))
low = 0
high = 8
found = 0

while low <= high:
    mid = int((high + low)/2)
    if array[mid] == find:
        found = 1
        print("Found at index {}".format(mid))
        break
    else:
        if array[mid] < find:
            low =int(mid + 1)
        else:
            high = int(mid - 1)

if found == 0:
    print("{} is not in the array.".format(find))
        
    

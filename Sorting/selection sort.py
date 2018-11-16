s = []
num = int(input("Enter the range of the set: "))

for x in range(num):
    items = int(input('Enter the number: '))
    s.append(items)

def select(s):
    for i in range(len(s)):
        for j in range(len(s)):
            if s[i] < s[j]:
                s[i], s[j] = s[j], s[i]
                print(s)
    print(s)

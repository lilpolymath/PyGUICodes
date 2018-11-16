bradct = {"[" : "]", "{" : "}", "(" : ")", "]" : "[",")" : "(", "}" : "{"}
string = str(input(""))
s = len(string)

if s%2 != 0:
    print("No")

else:
    h1 = []
    h2 = []
    for i in range(0, int(s/2)):
        h1.append(string[i])
        i += 1
    for j in range(int(s/2), s):
        h2.append(string[j])
        j += 1
    rev = h2[::-1]
    x = []

 for j in rev:
    x.append(bradct[j])

if h1 == x:
    print("Yes")

else:
    print("No")

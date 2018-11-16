#program to transpose a matrix

X = [[1,2],
	[3,4],
	[5,6]]

result = [[0,0,0],
		 [0,0,0]]

#iterate through rows
for i in range(len(X)):
	#iterate through cilumns
	for j in range(len(X[0])):
		result[j][i] = X[i][j]

for r in result:
	print(r)
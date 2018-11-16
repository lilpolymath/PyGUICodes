'''foods = ['bacon', 'tuna', 'ham','sausages','beef']
i = 1

for items in foods:
	print(items)
	print(len(items))
'''

'''for x in range(10):
	print("Jesus is Lord")
'''

'''confession = "Jesus is Lord"
x = 5
while x < 10:
	print(confession)
	x += 1
'''

magicNum = 26
#Program finds magic number

for n in range(101):
	if n is magicNum:
		print("Match Found")
		print(n, "is the Number")
		break
	else:
		print(n)
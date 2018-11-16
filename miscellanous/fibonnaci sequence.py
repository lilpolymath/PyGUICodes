import time

#Program to Display th Fibonnaci Sequence

#Changethis value to obtain different result
nterms = 10

#uncomment this part to take inout from the user
#nterms = int(input("How many terms? "))

# first two terms
n1 = 0
n2 = 1
count = 2

#check if the numberof terms is valid
if nterms <= 0:
	print("Please enter a positive Integer")
elif nterms == 1:
	print("Fibonnaci sequence unto", nterms, ": ")
	print(n1)
else:
	print("Fibonnaci sequence upto", nterms, ": ")
	print(n1,',',n2, end=',')
	while count < nterms:
		nth = n1 + n2
		print(nth, end=",")
		#To updating Values
		n1 = n2
		n2 = nth
		count += 1
time.sleep(5)
import time

def recur_fibo(n):
	"""Recursive function to
	print Fibonnaci sequence"""
	if n <= 1:
		return n
	else:
		return(recur_fibo(n-1) + recur_fibo(n-2))

#Change this value or a different result
nterms = 10

#uncomment to take input from the user
#nterms = int(input("How many terms? "))

#check if the number of terms is valid
if nterms <= 0:
	print("Please enter a positive integer")
else:
	print("Fibonnaci sequence: ")
	for i in range(nterms):
		print(recur_fibo(i))
time.sleep(5)
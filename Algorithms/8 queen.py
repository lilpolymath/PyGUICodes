#Solving the 8 queen Problem with Recursion
#The Solution is in Python 2.7

BOARD_SIZE = 8

def under_attack(col, queens):
	left = right = col

	for r,c in reversed(queens):
		left, right = left - 1, right + 1

		if c in (left, col, right):
			return True
		return False

def solve(n, solutions=None):
	if n == 0:
		return [[]]

	smaller_solutions = solve(n - 1)

	return [solutions + [(n, i + 1)]
		for i in xrange(BOARD_SIZE)
			for solution in smaller_solutions
				if not under_attack(i + 1, solution)

for inputs in solve(BOARD_SIZE):
    print(inputs)

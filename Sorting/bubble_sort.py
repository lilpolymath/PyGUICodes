def bubble_sort(seq):
	changed = True
	while changed:
		changed = False
		no = len(seq) - 1
		for i in range(no):
				if seq[i] > seq[i + 1]:
					seq[i], seq[i + 1] = seq[i + 1], seq[i]
					changed = True
	return None

bubble_sort(12354678)
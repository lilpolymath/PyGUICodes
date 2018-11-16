'''
Note that all codes are in python 2.7.6
This is a program that solves or finds
the Reverse Complement of a DNA Sequence
'''

def init(sequence):
	with open(argv[1]) as input:
		sequence = "".join([line.strip() for line in input.readlines()[1:]])
	return sequence

complement = {"A" : "T", "C" : "G", "G" : "C", "T" : "A"}

def reverse_complement(sequence):
	bases = [complement[base] for base in sequence]
	bases = reversed(bases)
	return bases

result = reverse_complement(sequence)
print("".join(result))

'''
def fasta_reader(filename):
	from Bio.SeqIO.FastaIO import FastaIterator
	with open(filename) as handle:
		for record in FastaIterator(handle):
			yield record
'''
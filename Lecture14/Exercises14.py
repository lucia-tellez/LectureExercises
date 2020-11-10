#!/usr/bin/python3

#EXERCISE 1
def PercentAA (ProtSeq, AA):
	length = len(ProtSeq)
	AA_count = ProtSeq.upper().count(AA.upper())
	Percent = (AA_count / length) * 100
	return Percent

assert (PercentAA("MSRSLLLRFLLFLLLLPPLP", "M")) == (5)
assert round(PercentAA("MSRSLLLRFLLFLLLLPPLP", "r")) == round(10)
assert round(PercentAA("MSRSLLLRFLLFLLLLPPLP", "L")) == round(50)
assert round(PercentAA("MSRSLLLRFLLFLLLLPPLP", "Y")) == round(0)

#EXERCISE 2: Pass a list of AA residues rather than one
def PercentAAs (ProtSeq, AAlist=['AILMFWYV']):
	length = len(ProtSeq)
	counter = 0
	for AA in AAlist:
		print("counting number of", AA)
		AA_count = ProtSeq.upper().count(AA.upper())
		counter = counter + AA_count
		print("running total is" + str(counter))
	Percent = (counter / length) * 100
	print("final percentage is" + str(Percent))
	return Percent

assert round(PercentAAs("MSRSLLLRFLLFLLLLPPLP", ["M"])) == 5
assert round(PercentAAs("MSRSLLLRFLLFLLLLPPLP", ['F', 'S', 'L'])) == 70
assert round(PercentAAs("MSRSLLLRFLLFLLLLPPLP")) == 65

#EXERCISE 3: Undetermined DNA base counter
def count_undetermined_1(dna):
    total_good_bases = 0
    for base in ['A', 'T', 'G', 'C']:
        total_good_bases = total_good_bases + dna.upper().count(base)
    return len(dna) - total_good_bases

count_undetermined_1('atucgtgractanctgactg')

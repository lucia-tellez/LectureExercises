
##!/usr/bin/python3

##Get the local DNA sequence
Local_dna = open("plain_genomic_seq.txt")
Local_dna = Local_dna.read()
Local_dna_1 = Local_dna.replace("\n","")

Exon1Local = Local_dna_1[:63]
Exon2Local = Local_dna_1[90:]

CodingSequence = FirstExon + SecondExon
CodingPercentage = (len(CodingSequence)/len(GenomicDNA))*100
print("The percentage of coding sequence in this DNA fragment is of", CodingPe$

#Print the original genomic sequence with introns in lowercase
Intron = GenomicDNA[63:89]
IntronLC = Intron.lower()
SequenceEX4 = FirstExon + IntronLC + SecondExon


#!/usr/bin/python3

##CHART WITH AT CONTENT OF E.COLI IN A SLIDING WINDOW
##Import necessary modules
import os
import matplotlib.pyplot as plt

ecoli = open("ecoli.txt").read().replace("\n","").upper()[0:100000]
window = 1000

#Empty list to hold our dinucleotide
at = []

#Iterate over all the starting positions
for start in range(len(ecoli) - window):
	win = ecoli[start:start+window]
	at.append((win.count("A")+win.count("T")) / window)
plt.figure(figsize=(20,10))
plt.plot(at, label="AT reps")
plt.ylabel("Overrepresentation")
plt.xlabel("Position on genome")
plt.legend
plt.savefig("ecoliAT.png", transparent=True)
plt.show()

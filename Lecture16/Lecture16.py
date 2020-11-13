#!/usr/bin/python3

import re

AccNumbers = ["xkn59438", "yhdck2", "eihd39d9", "chdsye847", "hedle3455", "xjhd53e", "45da", "de37dp"]

outputs = []

for AccN in AccNumbers:
	if re.search(r"5", AccN):
		outputs.append(AccN + " : contains number 5")
	if re.search(r"[de]", AccN):
		outputs.append(AccN + " : contains the letter d or e")
	if re.search(r"de", AccN):
		outputs.append(AccN + " : contains adjacent d and e")
	if re.search(r"d.*e", AccN): 
		outputs.append(AccN + " : contains d and e in that order, doesn't have to be adjacent")
		

outputs.sort()
print(('\n').join(outputs))

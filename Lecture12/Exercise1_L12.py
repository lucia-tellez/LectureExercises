#!/usr/bin/python3

##EXERCISE 1: PROCESSING DNA IN A FILE
#Trim the adapters (delete 14 first positions of each line)

my_input = open('input.txt', "r")
for line in my_input:
	no_adapt = (line[14:])
	print('The sequence length of line %line is' %(line))
	outfile = open("seq_no_adapters.txt", "a")
	outp = no_adapt + "\n"
	outfile.write(outp)
	outfile.close()

my_input.close()

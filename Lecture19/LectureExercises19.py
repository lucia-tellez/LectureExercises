#!/usr/bin/python3

import subprocess
from Bio import Entrez, SeqIO

##Enter NCBI API keys to handle more search requests
Entrez.email = "l.tellez.012@gmail.com"
Entrez.api_key=subprocess.check_output("echo $NCBI_API_KEY", shell=True).rstrip().decode()

'''
#Define the search
result = Entrez.read(Entrez.esearch(db="protein", term="Mammalia COX1 complete", retmax="20"))

##Extract info from the results of the search
count=1
for accession in result['IdList']:
    gb_file = Entrez.efetch(db="protein",id=accession,rettype="gb")
    record = SeqIO.read(gb_file, "genbank")
    print(count,record.id+"\t"+record.description+"\t"+record.seq)
    count += 1
    if count == 6 :
      break
'''
##GENERAL SCRIPT FOR ANY GENE AND ANY TAXONOMIC GROUP
TaxonID = input("Type in your taxon ID of interest: ")
Protein = input("Type in your gene of interest: ")
hola = '{} {}'.format(TaxonID, Protein)

print(hola)
resultgeneral = 'Entrez.read(Entrez.esearch(db="protein", term="{} {}", retmax="20"))'.format(TaxonID, Protein)

count=1
for accession in resultgeneral['IdList']:
    gb_file = Entrez.efetch(db="protein",id=accession,rettype="gb")
    record = SeqIO.read(gb_file, "genbank")
    print(count,record.id+"\t"+record.description+"\t"+record.seq)
    count += 1
    if count == 6 :
      break



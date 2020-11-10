#!/usr/bin/python3

gencode = {
'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W'}

#Function 1: define a function which gets the reverse sequence of your DNA sequence

def Compl_Seq(DNA_seq):
    Forward='ATCG'
    Reverse='TAGC'
    Reverse=str.maketrans(Forward, Reverse)
 #Creation of a table to translate ATCG to TAGC
    Seq_Comp=DNA_seq.translate(Reverse)
 #Change the sequence from 3'-->5' to 5'-->3' (direction with biological sense)

    Seq_Comp=Seq_Comp[::-1] 
    print("Complementary sequence:\t", Seq_Comp, "\n")  
    return(Seq_Comp)

#Function 2: define a function that translates your given DNA sequence with your given Genetic Code.

def translation(DNA_seq, GenCode_dic):
    protein_sequences=[]
    for frame in range(3): 
        Triplet_list=[]
        position=0+frame
        while -1<position<(len(DNA_seq)-2): 
##note that the last 2 positions are not considered the start of a codon
            triplet=DNA_seq[position]+DNA_seq[position+1]+DNA_seq[position+2]
            Triplet_list.append(triplet)
            position=position+3
        #create a list to append the aa's translated
        aa_list=[]
        for codon in Triplet_list:
            aa_list.append(GenCode_dic[codon])
        aa_seq=''.join(aa_list)
        protein_sequences.append(aa_seq)
    return(protein_sequences)

MySeq="ATGTTCGGT"
MySeqComp=Compl_Seq(MySeq)

protein_sequences=translation(MySeqComp,gencode)
print(protein_sequences)

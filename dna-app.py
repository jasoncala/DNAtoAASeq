import pandas as pd 
import streamlit as st 
import altair as alt 

def create_RNA(sequence):
	st.header("RNA Strand")
	complement = ""
	for c in sequence:
		add = ""
		if (c == 'G'):
			add+='C' 
		elif(c == 'C'):
			add+='G'
		elif(c=='A'):
			add+='U'
		elif(c=='T'):
			add+='A'
		complement+=add
	st.write("3'- "+ complement+" -5'")
	return complement

def build_AA(aaArray):
	aaStr = "Met(START) "
	for c in aaArray:
		if (c == 'UAA' or c == 'UAG' or c == 'UGA'):
			aaStr+= 'STOP'
			#stop codon
			break
		elif(c == 'UUU' or c == 'UUC'):
			aaStr+= 'Phe '
		elif(c == 'UUA' or c == 'UUG' or c == 'CUU' or c == 'CUC' or c == 'CUA' or c == 'CUG'):
			aaStr+= 'Leu '
		elif(c == 'AUU' or c == 'AUC' or c =='AUA'):
			aaStr+= 'Ile '
		elif(c == 'GUU' or c== 'GUC' or c== 'GUA' or c== 'GUG'):
			aaStr+= 'Val '
		elif(c == 'UCU' or c == 'UCC' or c == 'UCA' or c == 'UCG' or c == 'AGU' or c == 'AGC'):
			aaStr+= 'Ser '
		elif(c == 'CCU' or c == 'CCC' or c == 'CCA' or c == 'CCG'):
			aaStr+= 'Pro '
		elif(c == 'ACU' or c == 'ACC' or c == 'ACA' or c == 'ACG'):
			aaStr+= 'Thr '
		elif(c == 'GCU' or c == 'GCC' or c == 'GCA' or c == 'GCG'):
			aaStr+= 'Ala '
		elif(c == 'UAU' or c == 'UAC'):
			aaStr+= 'Tyr '
		elif(c == 'CAU' or c == 'CAC'):
			aaStr+= 'His '
		elif(c == 'CAA' or c == 'CAG'):
			aaStr+= 'Gln '
		elif(c == 'AAU' or c == 'AAC'):
			aaStr+= 'Asn '
		elif(c == 'AAA' or c == 'AAG'):
			aaStr+= 'Lys '
		elif(c == 'GAU' or c == 'GAC'):
			aaStr+= 'Asp '
		elif(c == 'GAA' or c == 'GAG'):
			aaStr+= 'Glu '
		elif(c == 'UGU' or c == 'UGC'):
			aaStr+= 'Cys '
		elif(c == 'UGG'):
			aaStr+= 'Trp '
		elif(c == 'CGU' or c == 'CGC' or c == 'CGA' or c == 'CGG' or c == 'AGA' or c == 'AGG'):
			aaStr+= 'Arg '
		elif(c == 'GGU' or c == 'GGC' or c == 'GGA' or c == 'GGG'):
			aaStr+= 'Gly '
	return aaStr

def create_AA(complement):
	if('AUG' in complement):
		ind = complement.find('AUG')
		complement = complement[ind:]
		aalist = ""
		codon = ""
		count = 0
		for c in complement:
			count+=1
			if(count<=3):
				codon+=c
				if(count == 3):
					count = 0
					aalist+=codon+" "
					codon = ""

		aaArray = aalist.split(' ')

		aaStr = build_AA(aaArray)
		
		st.header("Amino Acid Sequence")
		st.write(aaStr)

def main():
	st.write("""
	# DNA Nucleotide Analysis Web App

	This app performs basic analysis on a given nucleotide sequence!

	***
	""")

	sequence_input = "CAATACTATGGGCTCTTTATTGCCCGCATTCAT"

	sequence = st.text_area("Sequence input", sequence_input, height = 75)

	st.write("""
		***
		""")

	st.header("INPUT (DNA Sequence, 5' to 3')")
	st.write("5'- "+ sequence+" -3'")

	st.write("""
		***
		""")

	complement = create_RNA(sequence)
	create_AA(complement)

if __name__ == '__main__':
	main()
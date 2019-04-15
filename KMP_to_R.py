#KEGGmapper pathway to R script
#This code takes an input from KEGGmapper and creates an output in a format that can
#readily create a KEGG Pathway x sample matrix with the reshape2 package in R.  

#To run this code: python KMP_to_R.py -i <insert file path> -o ./ 
#Example files: python KMP_to_R.py -i WisconsinNP_annotated_pathway.txt -o ./

#Written by Damien Finn
#email: damien.finn@uqconnect.edu.au

import csv
import sys
import os.path
import re


def import_file(filename):
    for line in csv.reader(open(filename)):
        if line:
            yield line

input_file = sys.argv[sys.argv.index('-i')+1]
output_file = sys.argv[sys.argv.index('-o')+1]


input_liste = []


for line in import_file(input_file):
	for il in line:
		if il[0] is "0":
			tmp = il[:-1].split(' ')
			number = tmp[-1]
			number = number.replace('(', '')
			number = number.replace(')', '')
			KO = tmp[0:-1]
			KO = '_'.join(KO)
			input_liste.append(input_file + '\t' + KO + '\t' + str(number))
		else:
			pass
		
		
output = open(os.path.join(output_file, input_file + "KMP_to_R.txt"), "w")

for x in input_liste:
	output.write(x + '\n')









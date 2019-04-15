#KO_counter for collating KO terms from JGI outputs into a format that can readily make
#a matrix of KOs x samples in R with the reshape2 package. An integer for standardising a
#randomly selected subset of KOs from the sample must be chosen. This is to better compare
#samples with slightly varying sequencing depth. A count from the smaller sample should
#be chosen. For example, if comparing a sample with 640 000 versus 520 000 sequences, 
#the -n should be 520000.

#This script creates two outputs - one is a list of specific KOs the user may be interested
#in (my_KO_counts.txt) and a list of all KOs in the sample (all_KO_counts.txt).

#To run this code: python KO_counter.py -i <insert file path> -o ./ -n <number of randomly selected KOs to standardize to>
#For the example files: python KO_counter.py -i Wisconsin_NP_12805.assembled.faa.ko -o ./ -n 792000

#Written by Damien Finn
#email: damien.finn@uqconnect.edu.au


import csv
import sys
import os.path
import random
from collections import Counter

def import_file(filename):
    for line in csv.reader(open(filename)):
        if line:
            yield line

input_file = sys.argv[sys.argv.index('-i')+1]
output_file = sys.argv[sys.argv.index('-o')+1]
ran_sam_no = sys.argv[sys.argv.index('-n')+1]

#This is a user defined list of specific KO terms that will be searched for within all KOs
myKOs =["K02588", "K01183", "K01179", "K01181", "K17641"]


input_liste = []
standard_liste = []
tmp = []
output_liste = []

for line in import_file(input_file):
	for il in line:
		sp_line = il.split('\t')
		KO = sp_line[2] 
		input_liste.append(KO)

tmp_ran = random.sample(input_liste, int(ran_sam_no))

	
for x in tmp_ran:
	tmp.append(x[3:])

for K in myKOs:
	for line in tmp:
		if K in line:
			output_liste.append(K)

	
Sums_of_counts = Counter(output_liste)		

output = open(os.path.join(output_file, input_file + "my_KO_counts.txt"), "w")

for key, value in Sums_of_counts.items():
    output.write(input_file + '\t' + key + '\t' + str(value) + '\n')
    
output2 = open(os.path.join(output_file, input_file + "all_KO_counts.txt"), "w")

Sums_of_counts2 = Counter(tmp)

for key, value in Sums_of_counts2.items():
    output2.write(input_file + '\t' + key + '\t' + str(value) + '\n')










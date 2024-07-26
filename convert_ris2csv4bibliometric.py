import pandas as pd

file=open('asreview_dataset_all_IBS_permeability_.ris','r')
extracted_list=[]
for x in file:
	if 'TI' in x.strip().split('  -')[0]:
		dictionary={'N1': [], 'TI':x.strip().split('  -')[1],'AB': ''}
		extracted_list.append(dictionary)
	if 'AB'  in x.strip().split('  -')[0]:
		extracted_list[-1]['AB']+=x.strip().split('  -')[1]
	if 'N1' in x.strip().split('  -')[0]:
		extracted_list[-1]['N1'].append(x.strip().split('  -')[1])




print(len(extracted_list))
file1=open('per_Nica1_.txt', 'w')

for x in extracted_list:
	file1.write(str(x)+'\n')




#### STEP 1
RIS_relevant_file=open('02_ASReview_RELEVANT_IBS_permeability.ris','r')#### open RELEVANT ris file, that contains only relevant records

relevant_titles=[]

for x in RIS_relevant_file:
	if 'TI  -' in x:
		relevant_titles.append(x.strip().split('TI  -')[1])#### Titles extraction from relevant ris file


### STEP 2
### filtering scopus csv file in order to contain only RELEVANT 

CSV_file_input=open('00_IBS_permeability_scopus.csv','r')            ### open scopus csv file 
CSV_file_ouput=open('02_ASReview_RELEVANT_IBS_permeability.csv','w') ### save csv file containing only relevant 



lista_estratti=[]
for x in CSV_file_input:
	if '"Authors","Author full names",'in x:
		CSV_file_ouput.write(x+'\n')### writing intestation
	else:
		for y in relevant_titles:
			if '"'+y.strip()+'"' in x:
				CSV_file_ouput.write(x+'\n') ### this loop is useful to filter scopus csv file

CSV_file_ouput.close
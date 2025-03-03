## A)  In this project data and pipelines for the following paper are described: '	Mapping Research Trends on Intestinal Permeability in Irritable Bowel Syndrome with a Focus on Nutrition: A Bibliometric Analysis'.
## The scopus dataset were saved in files: 
## 1) 00_IBS_permeability_scopus.csv; 
## 2) 00_IBS_permeability_scopus.ris.
## Both the files contain scopus records for the given query:
TITLE-ABS-KEY ( ( "intestin* barrier*" OR "gut barrier*" OR "intestin* permeability" OR "epithelial barrier*" OR "leaky gut" ) AND ( ibs OR "Irritable Bowel syndrome" ) ) AND ( LIMIT-TO ( DOCTYPE , "ar" ) ) AND ( LIMIT-TO ( LANGUAGE , "English" ) )

## B) The file 01_DEDUPLICATED_IBS_permeability_scopus.ris, contains unique records downloaded from scopus database ; 
## C) The file 02_ASReview_RELEVANT_IBS_permeability.ris, contains only RELEVANT records obtained by the Active machine learning ASReview. In this file, the irrilevant or not_seen records are omitted. 
## Note, for not_seen records are intented those records that are not relevant for ASReview, specifically that are not evaluated manually using active machine learning approach. 
## D) convert_ris2csv4bibliometric.py contains a python code to filter scopus csv dataset for relevant records. The  convert_ris2csv4bibliometric.py output file is compatible with R bibliometix package.
## E) the file: 02_ASReview_RELEVANT_IBS_permeability.csv is the output of the filter_scopus_CSV4Relevant_records.py pipeline. 



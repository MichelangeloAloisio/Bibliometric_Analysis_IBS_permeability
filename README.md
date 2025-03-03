Project Overview: Mapping Research Trends on Intestinal Permeability in Irritable Bowel Syndrome with a Focus on Nutrition

A) Dataset Description
Scopus Dataset Files :
00_IBS_permeability_scopus.csv: Contains Scopus records for the query.
00_IBS_permeability_scopus.ris: RIS format of the same Scopus records.
Query used: to download ris and csv from Scopus documents
TITLE-ABS-KEY ( ( "intestin* barrier*" OR "gut barrier*" OR "intestin* permeability" OR "epithelial barrier*" OR "leaky gut" ) AND ( ibs OR "Irritable Bowel syndrome" ) ) AND ( LIMIT-TO ( DOCTYPE , "ar" ) ) AND ( LIMIT-TO ( LANGUAGE , "English" ) )


B) Deduplication
01_DEDUPLICATED_IBS_permeability_scopus.ris: Contains unique records after deduplication.

C) Relevance Filtering
02_ASReview_RELEVANT_IBS_permeability.ris: Relevant records identified using ASReview's active machine learning approach. Irrelevant or unseen records are excluded.

D) Publication and Citation Analysis
03_plot_publication_per_year&citation.xlsx: Excel file with formulas to generate publication and citation plots over time.

E) Word Cloud Customization
04_keywords_removed_from_WordCloudplot.txt: List of irrelevant words removed from the Word Cloud plot.

F) Dietary Records Filtering
05_FILTERED_100_dietary_scopus_papers.csv: Records filtered from 02_ASReview_RELEVANT_IBS_permeability.csv focusing on dietary aspects.

G) Python Code for Data Processing
convert_ris2csv4bibliometric.py: Converts RIS files to CSV format compatible with the R bibliometrix package.

H) Relevant Records Extraction
filter_scopus_CSV4Relevant_records.py: Pipeline to extract relevant records from the Scopus CSV dataset.

I) Dietary Filtering Script
p02_filtering_dieta_from_ris.py: Python script to filter records related to diet from 02_ASReview_RELEVANT_IBS_permeability.ris into 05_FILTERED_100_dietary_scopus_papers.csv.



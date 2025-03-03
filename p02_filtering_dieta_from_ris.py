######## Pipeline to filter scopus dataset based on Nutrition


import pandas as pd

# Keywords definition
keywords_nutrition = ["nutrition", "diet", "food", "nutrient", "microbiome", "microbiota", "probiotic", "prebiotic"]

# Dataframe Upload
df = pd.read_csv('02_ASReview_RELEVANT_IBS_permeability.csv')

print(df)


# Dataframe Filtering
df_nutrition = df[df.apply(lambda row: any(kw in str(row["Title"]).lower() or  kw in str(row["Abstract"]).lower() or kw in str(row["Author Keywords"]).lower() for kw in keywords_nutrition), axis=1)]
print(df_nutrition)

df_nutrition.to_csv("FILTERED_100_dietary_scopus_papers.csv", index=False, sep='^')
#exit()



### extract author ID to counts
df_nutrition['Author IDs'] = df_nutrition['Author full names'].str.extractall(r'\((.*?)\)').unstack().apply(lambda x: ', '.join(x.dropna()), axis=1)



print(df_nutrition['Author IDs'])# Visualizza il risultato
#print(df[['Author full names', 'Author IDs']])
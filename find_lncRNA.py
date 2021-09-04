import pandas as pd
import os

# get all the different gene names in our expression data
names = set()
dir = 'Differential Expression results'
for file_name in os.listdir(dir):
    file_path = os.path.join(dir, file_name)
    df = pd.read_csv(file_path)
    names.update([ens_id for ens_id, gene_name in df['Unnamed: 0'].str.split('_')])

# export the ENSG names to use with biomart
f = open('genes.txt', 'w')
f.writelines([",".join(sorted(list(names)))])
f.close()

# result of biomart:
df = pd.read_csv('genes_transcript_type_ncbi_kegg.csv')
df.columns = ['gene_id', 'type', 'ncbi', 'kegg']
df.to_csv('genes_transcript_type_ncbi_kegg.csv', index=False)

# get only unique row per Gene stable ID
unique = df.sort_values('gene_id').groupby(['gene_id']).first().reset_index()
unique.to_csv('genes_transcript_type_ncbi_kegg_unique.csv', index=False)


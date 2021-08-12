import pandas as pd

# from biomart
kidney = pd.read_csv('housekeeping_kidney.csv')
unique = kidney.sort_values('GeneID').groupby(['GeneID']).first().reset_index()
unique.to_csv('housekeeping_kidney.csv', index=False)

# from niomart
brain = pd.read_csv('housekeeping_brain.csv')
unique = brain.sort_values('GeneID').groupby(['GeneID']).first().reset_index()
unique.to_csv('housekeeping_brain.csv', index=False)
import pandas as pd

# from biomart
general = pd.read_csv('housekeeping_general.csv')
unique = general.sort_values('GeneID').groupby(['GeneID']).first().reset_index()
unique.to_csv('housekeeping_general.csv', index=False)

# from niomart
brain = pd.read_csv('housekeeping_brain.csv')
unique = brain.sort_values('GeneID').groupby(['GeneID']).first().reset_index()
unique.to_csv('housekeeping_brain.csv', index=False)

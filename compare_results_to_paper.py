import pandas as pd

# https://www.oncotarget.com/article/12122/text/
paper_results = pd.read_csv('E-GEOD-78936-query-results.tsv', sep='\t')
paper_results.columns = ['Gene ID', 'Gene Name',
                         'bd_vs_norm_ba11.log2FoldChange', 'bd_vs_norm_ba11.adjpvalue',
                         'bd_vs_norm_ba24.log2FoldChange', 'bd_vs_norm_ba24.adjpvalue',
                         'bd_vs_norm_ba9.log2FoldChange', 'bd_vs_norm_ba9.adjpvalue',
                         'sz_vs_norm_ba11.log2FoldChange', 'sz_vs_norm_ba11.adjpvalue',
                         'sz_vs_norm_ba24.log2FoldChange', 'sz_vs_norm_ba24.adjpvalue',
                         'sz_vs_norm_ba9.log2FoldChange', 'sz_vs_norm_ba9.adjpvalue',
                         ]

# our results
columns = ['Gene ID', 'log2FoldChange', 'padj']
bd_vs_norm_ba9 = pd.read_csv('bipolar_disorder VS. normal BA9 .csv')
bd_vs_norm_ba9['Gene ID'] = [string.split('_')[0] for string in bd_vs_norm_ba9['Unnamed: 0']]
bd_vs_norm_ba9 = bd_vs_norm_ba9[columns]
bd_vs_norm_ba9 = pd.merge(left=bd_vs_norm_ba9,
                          right=paper_results[['bd_vs_norm_ba9.log2FoldChange', 'bd_vs_norm_ba9.adjpvalue', 'Gene ID']],
                          how='right',
                          on='Gene ID')
bd_vs_norm_ba11 = pd.read_csv('bipolar_disorder VS. normal BA11 .csv')
bd_vs_norm_ba11['Gene ID'] = [string.split('_')[0] for string in bd_vs_norm_ba11['Unnamed: 0']]
bd_vs_norm_ba11 = bd_vs_norm_ba11[columns]
bd_vs_norm_ba11 = pd.merge(left=bd_vs_norm_ba11,
                           right=paper_results[['bd_vs_norm_ba11.log2FoldChange', 'bd_vs_norm_ba11.adjpvalue', 'Gene ID']],
                           how='right',
                           on='Gene ID')
bd_vs_norm_ba24 = pd.read_csv('bipolar_disorder VS. normal BA24 .csv')
bd_vs_norm_ba24['Gene ID'] = [string.split('_')[0] for string in bd_vs_norm_ba24['Unnamed: 0']]
bd_vs_norm_ba24 = bd_vs_norm_ba24[columns]
bd_vs_norm_ba24 = pd.merge(left=bd_vs_norm_ba24,
                           right=paper_results[['bd_vs_norm_ba24.log2FoldChange', 'bd_vs_norm_ba24.adjpvalue', 'Gene ID']],
                           how='right',
                           on='Gene ID')

sz_vs_norm_ba9 = pd.read_csv('schizophrenia VS. normal BA9 .csv')
sz_vs_norm_ba9['Gene ID'] = [string.split('_')[0] for string in sz_vs_norm_ba9['Unnamed: 0']]
sz_vs_norm_ba9 = sz_vs_norm_ba9[columns]
sz_vs_norm_ba9 = pd.merge(left=sz_vs_norm_ba9,
                          right=paper_results[['sz_vs_norm_ba9.log2FoldChange', 'sz_vs_norm_ba9.adjpvalue', 'Gene ID']],
                          how='right',
                          on='Gene ID')
sz_vs_norm_ba11 = pd.read_csv('schizophrenia VS. normal BA11 .csv')
sz_vs_norm_ba11['Gene ID'] = [string.split('_')[0] for string in sz_vs_norm_ba11['Unnamed: 0']]
sz_vs_norm_ba11 = sz_vs_norm_ba11[columns]
sz_vs_norm_ba11 = pd.merge(left=sz_vs_norm_ba11,
                           right=paper_results[['sz_vs_norm_ba11.log2FoldChange', 'sz_vs_norm_ba11.adjpvalue', 'Gene ID']],
                           how='right',
                           on='Gene ID')
sz_vs_norm_ba24 = pd.read_csv('schizophrenia VS. normal BA24 .csv')
sz_vs_norm_ba24['Gene ID'] = [string.split('_')[0] for string in sz_vs_norm_ba24['Unnamed: 0']]
sz_vs_norm_ba24 = sz_vs_norm_ba24[columns]
sz_vs_norm_ba24 = pd.merge(left=sz_vs_norm_ba24,
                           right=paper_results[['sz_vs_norm_ba24.log2FoldChange', 'sz_vs_norm_ba24.adjpvalue', 'Gene ID']],
                           how='right',
                           on='Gene ID')

for k, df in {'bd_vs_norm_ba9': bd_vs_norm_ba9,
              'bd_vs_norm_ba11': bd_vs_norm_ba11,
              'bd_vs_norm_ba24': bd_vs_norm_ba24,
              'sz_vs_norm_ba9': sz_vs_norm_ba9,
              'sz_vs_norm_ba11': sz_vs_norm_ba11,
              'sz_vs_norm_ba24': sz_vs_norm_ba24}.items():
    print(f"{''.join(['*'] * 20)} {k} Gomafu MIAT {''.join(['*'] * 20)}")
    gomafu_df = df[df['Gene ID'] == 'ENSG00000225783']
    print(gomafu_df.iloc[0])

    print(f"{''.join(['*'] * 20)} {k} DISC1 {''.join(['*'] * 20)}")
    disc1_df = df[df['Gene ID'] == 'ENSG00000162946']
    print(disc1_df.iloc[0])

    print(f"{''.join(['*'] * 20)} {k} ERBB4 {''.join(['*'] * 20)}")
    erbb4_df = df[df['Gene ID'] == 'ENSG00000178568']
    print(erbb4_df.iloc[0])

    print(f'Mean difference between log2FoldChanges (ours minus original, over all genes): '
          f'{(df[df.columns[1]] - df[df.columns[3]]).mean()}')
    print(f'Mean difference between adj-pvalue (ours minus original, over all genes): '
          f'{(df[df.columns[2]] - df[df.columns[4]]).mean()}')

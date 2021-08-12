"""
Find the significant genes from experiment 1 - 6 for different normalization techniques (housekeeping genes)
"""
import pandas as pd
import os


raw_counts = pd.read_csv('E-GEOD-78936-raw-counts.tsv', sep='\t').set_index('GeneName')
norm = ''  # choice from ['', '_kidney', '_brain']
for norm in ['', '_kidney', '_brain']:
    dir = 'Differential Expression results'
    dir = (dir + " " + norm[1:] + ' norm') if norm else 'Differential Expression results no norm'
    significant = pd.read_csv(f'up_down_reg_genes_per_experiment{norm}.csv')
    biomart_data = pd.read_csv('genes_transcript_type_ncbi_kegg_unique.csv').set_index('gene_id')

    results = pd.DataFrame(columns=['Exp', 'GeneName', 'Up/Down'])
    exp, all_genes, regulated = [], [], []
    for i in range(len(significant)):
        for reg in ['up', 'down']:
            genes = significant.iloc[i][f'{reg}.reg']
            if type(genes) == str:
                genes = [gene.strip() for gene in genes.split(',')]
                all_genes.extend(genes)
                regulated.extend([reg] * len(genes))
                exp.extend([i + 1] * len(genes))

    results['Exp'] = exp
    results['GeneName'] = all_genes
    results['Up/Down'] = regulated
    results['GeneID'] = [raw_counts.loc[GeneName]['GeneID'] for GeneName in results.GeneName]
    results['KeggID'] = [biomart_data.loc[GeneID]['kegg'] if GeneID in biomart_data.index else None
                         for GeneID in results.GeneID]
    results['NcbiID'] = [biomart_data.loc[GeneID]['ncbi'] if GeneID in biomart_data.index else None
                         for GeneID in results.GeneID]
    results['type'] = [biomart_data.loc[GeneID]['type'] if GeneID in biomart_data.index else None
                       for GeneID in results.GeneID]

    # Read our own Differential Expression analysis results to append to `result`
    experiments_de_dfs = {path.split(" ")[0]: pd.read_csv(os.path.join(dir, path)).set_index('Unnamed: 0')
                          for path in sorted(os.listdir(dir)) if path.startswith('exp')}

    padj, log2FC = [], []
    for exp, GeneID, GeneName in zip(results['Exp'], results['GeneID'], results['GeneName']):
        df = experiments_de_dfs[f'exp{exp}']
        padj.append(df.loc[f'{GeneID}_{GeneName}'].padj if f'{GeneID}_{GeneName}' in df.index else None)
        log2FC.append(df.loc[f'{GeneID}_{GeneName}'].log2FoldChange if f'{GeneID}_{GeneName}' in df.index else None)

    results['adj.P.Val'] = padj
    results['logFC'] = log2FC
    results = results.rename(columns={'GeneName': 'Gene.symbol'})
    results.to_csv(f'significant_genes_by_experiment{norm if norm else "_no_norm"}.csv', index=False)

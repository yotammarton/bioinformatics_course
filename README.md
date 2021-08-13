# 236523 - Introduction to Bioinformatics
## ![image](https://user-images.githubusercontent.com/43007010/129244877-92615d82-ad39-429d-ad8d-f5eb8c5be091.png)

Ben Filiarsky	, Yotam Martin

## Abstract
Schizophrenia (SZ) and Bipolar Disorder (BD) are serious neuropsychiatric disorders, severely harming patients' life quality. In this work, we perform a GWAS on RNAseq reads obtained from postmortem brain samples, from three different brain regions. We perform differential expression analysis (DEA) and successfully recover results of the paper our work is based on (Hu et al., 2016). As a part of our analysis, we compare DEA results with no normalization by housekeeping genes (HKG), with normalization by a general HKG set and with a gene set specifically tailored for postmortem brain samples. We show that using a custom-fit gene set for such correction is beneficial and encourage future usage of specifically tailored gene sets for correction. Significantly up and down regulated genes are then enriched using KEGG enrichment, resulting in a substantial enrichment of the MAPK signaling pathway in SZ samples in the BA9 brain region, a pathway that had been previously linked to SZ. An additional weighted gene co-expression analysis (WGCNA) combined with clustering was performed, followed by functional enrichment (GO and DO) of each cluster. In all the experiments we found a cluster with a significantly enriched term that had been tightly connected to SZ and BD development in previous works. We finish our work with raising ethical concerns regarding usage of such research in future applications. Our code repository and all the data for this work as well as results and plots are available via GitHub.

#### Project tree:
.
├── Differential Expression Analysis
│   ├── Differential Expression results brain norm
│   │   ├── exp1 brain schizophrenia VS. normal BA9 .csv
│   │   ├── ...
│   │   └── exp6 brain bipolar_disorder VS. normal BA24 .csv
│   ├── Differential Expression results general norm
│   │   ├── exp1 general schizophrenia VS. normal BA9 .csv
│   │   ├── ...
│   │   └── exp6 general bipolar_disorder VS. normal BA24 .csv
│   ├── Differential Expression results no norm
│   │   ├── exp1 no_norm schizophrenia VS. normal BA9 .csv
│   │   ├── ...
│   │   └── exp6 no_norm bipolar_disorder VS. normal BA24 .csv
│   └── DifferentialExpressionPlots
│       ├── Heatmap_down
│       │   ├── exp1
│       │   │   ├── brain.tiff
│       │   │   ├── general.tiff
│       │   │   └── no_norm.tiff
│       │   └── ...
│       ├── Heatmap_up
│       ├── Kmeans_tSNE
│       ├── QQ
│       └── Volcano
├── Differential Expression Analysis.Rmd
├── E-GEOD-78936-atlasExperimentSummary.Rdata
├── E-GEOD-78936-query-results.tsv
├── E-GEOD-78936-raw-counts.tsv
├── Pathway Enrichment Analysis
│   └── pathfindR
│       ├── brain_norm
│       │   └── pathfindR_Results_exp_1_brain
│       ├── general_norm
│       │   └── pathfindR_Results_exp_1_general
│       └── no_norm
│           ├── pathfindR_Results_exp_1
│           ├── pathfindR_Results_exp_1_3_5
│           ├── pathfindR_Results_exp_3
│           └── pathfindR_Results_exp_5
├── Pathway Enrichment Analysis.Rmd
├── Weighted Gene Co-Expression Analysis
│   ├── Nets
│   └── Plots
│       ├── DO
│       ├── GO
├── Weighted Gene Co-Expression Analysis.Rmd
├── compare_results_to_paper.py
├── final_project_guidelines.pdf
├── find_lncRNA.py
├── genes_transcript_type_ncbi_kegg.csv
├── genes_transcript_type_ncbi_kegg_unique.csv
├── housekeeping_brain.csv
├── housekeeping_general.csv
├── general and brain keeping genes processing.py
├── significant_genes_by_experiment_brain.csv
├── significant_genes_by_experiment_general.csv
├── significant_genes_by_experiment_no_norm.csv
├── significant_genes_exp_1_to_6.py
├── up_down_reg_genes_per_experiment.csv
├── up_down_reg_genes_per_experiment_brain.csv
└── up_down_reg_genes_per_experiment_general.csv

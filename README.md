# ResFinder_FG_Analysis
Scripts for the analysis included in the manuscript

## Version comparison
Number of ARGs found in ResFinderFG v2.0 and v1.0 was compared using the following scripts :
    comparison_atb_rfg1vs2.py  (to compare gene numbers regarding antibiotic families)
    comparison_source_rf1vs2.py (to compare gene numbers regarding original sample source)
Then, comparison_plot.Rmd was used with R to generate the figure.

## Abricate analysis
Abricate was use with default parameters and 5 different antibiotic resistance genes databases (ResFinderFG v2.0, ResFinder 4.0, CARD, ARG-ANNOT and NCBI) to detect antibiotic resistance genes in 3 global microbial gene catalog (GMGC, https://gmgc.embl.de/download.cgi) :
      Human gut
      Soil
      Water (freshwater + marine)

## Antibiotic families classification
Antibiotic families were chosen using a deduplicated list of gene names obtained with each database and specific gene classification tables were made for each database. 

## Abricate results comparison regarding database used
Unigene hits were then categorized by gene catalog and information such as gene families (with the need of database specific gene classification table) were added using the folowing scripts :
      script_hits_retriever_gut.py
      script_hits_retriever_soil.py
      script_hits_retriever_water.py
And all the unigene hits obtained within one environment were concatenated into one table :
      hits_gut_all.csv
      all_soil.csv
      all_water.csv
To generate the upset plots, first, duplicate unigene_hits were remove using the script duplicate.py
Then, the following R scripts were used :
      upset_gut.csv
      upset_soil.csv
      upset_water.csv
To retrieve statistics such as number of unigene hits, specific unigene hits regarding database used and antibiotic families, we used stats_extract_dataframe_upset.py
Retrieved statistics were then written in the data.csv tables.

## Specific unigene hits gene names
First, specific unigene hits were retrieved using : exclusive_genes.py
Second, gene names were retrieved using specific_gene_names.py
